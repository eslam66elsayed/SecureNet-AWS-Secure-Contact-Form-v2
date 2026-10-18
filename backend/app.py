import os
import boto3
import pymysql
from dotenv import load_dotenv
from flask import Flask, jsonify, request

load_dotenv('/home/ssm-user/contact-api/.env')
app = Flask(__name__)

sns = boto3.client('sns', region_name=os.environ.get('AWS_REGION', 'us-east-1'))


def get_db_connection():
    return pymysql.connect(
        host=os.environ['DB_HOST'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        database=os.environ['DB_NAME'],
        port=int(os.environ.get('DB_PORT', '3306')),
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )


def notify_admin(submission):
    message = (
        'A new SecureNet contact submission was confirmed.\n'
        f"Name: {submission.get('name', 'Not provided')}\n"
        f"Email: {submission.get('email', 'Not provided')}\n"
        f"Subject: {submission.get('subject', 'Not provided')}\n"
        'Please review the submission.'
    )
    response = sns.publish(
        TopicArn=os.environ['SNS_TOPIC_ARN'],
        Subject='SecureNet - New Contact Submission',
        Message=message
    )
    return response['MessageId']


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200


@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json(silent=True) or {}
    name = str(data.get('name', '')).strip()
    email = str(data.get('email', '')).strip()
    subject = str(data.get('subject', '')).strip()
    message = str(data.get('message', '')).strip()

    if not name or not email or not subject or not message:
        return jsonify({'error': 'name, email, subject and message are required'}), 400
    if len(name) > 120 or len(email) > 255 or len(subject) > 255:
        return jsonify({'error': 'One or more fields are too long'}), 400
    if len(message) > 5000:
        return jsonify({'error': 'Message is too long'}), 400

    connection = None
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute(
                '''INSERT INTO contact_messages (name, email, subject, message)
                   VALUES (%s, %s, %s, %s)''',
                (name, email, subject, message)
            )
            submission_id = cursor.lastrowid
        connection.commit()

        sns_message_id = None
        try:
            sns_message_id = notify_admin({'name': name, 'email': email, 'subject': subject})
        except Exception:
            app.logger.exception('SNS notification failed')

        return jsonify({'status': 'success', 'id': submission_id, 'sns_message_id': sns_message_id}), 201
    except Exception:
        if connection:
            connection.rollback()
        app.logger.exception('Contact submission failed')
        return jsonify({'error': 'Unable to process the submission'}), 500
    finally:
        if connection:
            connection.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

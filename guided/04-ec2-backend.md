# 04 — EC2 Backend Configuration

## Instances

```text
10.0.11.131
10.0.12.251
```

The instances run in private application subnets.

## Stack

```text
Linux
Python
Flask
Gunicorn
systemd
```

## Application Directory

```text
/home/ssm-user/contact-api
```

## Environment File

Create:

```text
/home/ssm-user/contact-api/.env
```

Example:

```env
DB_HOST=<RDS-ENDPOINT>
DB_USER=admin
DB_PASSWORD=<DATABASE-PASSWORD>
DB_NAME=securenet
DB_PORT=3306
AWS_REGION=us-east-1
SNS_TOPIC_ARN=<SNS-TOPIC-ARN>
```

Never commit `.env` to GitHub.

## Dependencies

```bash
pip3 install -r requirements.txt
```

## Gunicorn

```bash
gunicorn --workers 3 --bind 0.0.0.0:5000 app:app
```

## systemd

```bash
sudo systemctl status contact-api --no-pager
sudo systemctl restart contact-api
sudo systemctl enable contact-api
```

## Health Test

```bash
curl http://127.0.0.1:5000/health
```

Expected response:

```json
{"status":"healthy"}
```

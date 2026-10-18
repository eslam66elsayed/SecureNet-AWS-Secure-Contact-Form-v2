# 04 — EC2 Backend Configuration

## EC2 Instances

The backend runs on two EC2 instances.

Private IPs:

```text
10.0.11.131
10.0.12.251
```

The instances are located in different Availability Zones.

## Backend Stack

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

## Install Python dependencies

```bash
pip3 install -r requirements.txt
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

Do not commit `.env` to GitHub.

## Test Flask

```bash
python3 app.py
```

## Production Server

Gunicorn is used instead of Flask's development server.

Example:

```bash
gunicorn --workers 3 --bind 0.0.0.0:5000 app:app
```

## systemd

Service:

```text
contact-api.service
```

Check status:

```bash
sudo systemctl status contact-api --no-pager
```

Restart:

```bash
sudo systemctl restart contact-api
```

Enable at boot:

```bash
sudo systemctl enable contact-api
```

## Health Test

```bash
curl http://127.0.0.1:5000/health
```

Expected:

```json
{
  "status": "healthy"
}
```
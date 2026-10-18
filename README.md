# SecureNet AWS Secure Contact Form

A secure AWS contact form application using a multi-tier architecture.

## Architecture

```text
Internet
   |
CloudFront
   |
S3 Frontend
   |
ALB
   |
Private EC2 (Flask/Gunicorn)
   |
Private RDS MySQL
   |
SNS Notification
```

## AWS Services

- Amazon VPC
- Public and Private Subnets
- Internet Gateway
- Application Load Balancer
- EC2
- RDS MySQL
- S3
- CloudFront
- AWS WAF
- AWS Shield
- Systems Manager
- VPC Endpoints
- SNS
- VPC Flow Logs
- Athena
- CloudWatch
- Transit Gateway
- IAM

## Network

VPC: `10.0.0.0/16`

Public subnets:
- `10.0.1.0/24` — us-east-1a
- `10.0.2.0/24` — us-east-1b

Private application subnets:
- `10.0.11.0/24` — us-east-1a
- `10.0.12.0/24` — us-east-1b

Private database subnets:
- `10.0.21.0/24` — us-east-1a
- `10.0.22.0/24` — us-east-1b

## Backend

The backend uses Python, Flask, Gunicorn and systemd.

Application port: `5000`

Endpoints:

```text
GET  /health
POST /api/contact
```

Two EC2 instances host the backend in private application subnets.

## Database

RDS MySQL is deployed in private database subnets.

Database:
`securenet`

Port:
`3306`

Table:
`contact_messages`

The RDS security group allows MySQL traffic only from the EC2 application security group.

## ALB

The Application Load Balancer distributes traffic to the EC2 instances.

Target port: `5000`

Health check:

```text
/health
```

## S3 and CloudFront

S3 stores the static frontend:

```text
index.html
style.css
script.js
```

CloudFront provides HTTPS, CDN delivery, caching and WAF integration.

## WAF and Shield

AWS WAF protects the web application from common malicious requests.

AWS Shield provides DDoS protection.

## Systems Manager

Systems Manager Session Manager is used to administer private EC2 instances without exposing SSH to the Internet.

Configured interface endpoints include:

```text
com.amazonaws.us-east-1.ssm
com.amazonaws.us-east-1.ssmmessages
```

An S3 Gateway Endpoint is also configured.

## SNS

SNS topic:

`SecureNet-Admin-Notifications`

After the database transaction succeeds, the application publishes a notification to SNS.

## Monitoring

CloudWatch monitors infrastructure metrics and alarms.

VPC Flow Logs are delivered to S3 and can be analyzed with Athena.

## Transit Gateway

The project demonstrates connectivity between:

```text
Main VPC:    10.0.0.0/16
Second VPC:  10.1.0.0/16
```

using AWS Transit Gateway.

## Security Principles

- Least privilege
- Network segmentation
- Private application servers
- Private database
- Security Group references
- Systems Manager instead of public SSH
- VPC endpoints
- WAF and Shield
- Flow Logs and CloudWatch
- Secrets excluded from Git

## Project Structure

```text
SecureNet-AWS-Secure-Contact-Form/
├── README.md
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── .env.example
│   └── systemd/
│       └── contact-api.service
├── guided/
└── images/
```

## Author

Eslam Elsayed  
Communications and Networks Engineering Student  
Cloud Computing & AWS Security Trainee

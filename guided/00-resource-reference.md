# 00 — Resource Reference

## Region

`us-east-1`

## VPC

Name: `Secure-Network-VPC`  
CIDR: `10.0.0.0/16`

## Subnets

Public:
- `10.0.1.0/24`
- `10.0.2.0/24`

Private Application:
- `10.0.11.0/24`
- `10.0.12.0/24`

Private Database:
- `10.0.21.0/24`
- `10.0.22.0/24`

## EC2

Private IPs:
- `10.0.11.131`
- `10.0.12.251`

Application: Flask + Gunicorn  
Port: `5000`  
Service: `contact-api`

## ALB

DNS:
`contactform-ALB-1366953573.us-east-1.elb.amazonaws.com`

Target port: `5000`  
Health check: `/health`

## RDS

Engine: MySQL  
Database: `securenet`  
Port: `3306`  
Table: `contact_messages`

## S3

Bucket:
`secure-network-origin-123`

## CloudFront

Distribution ID:
`E1YUP14VLB6ENI`

## SNS

Topic:
`SecureNet-Admin-Notifications`

## Systems Manager Endpoints

- `com.amazonaws.us-east-1.ssm`
- `com.amazonaws.us-east-1.ssmmessages`

## Transit Gateway Networks

- Main VPC: `10.0.0.0/16`
- Connected VPC: `10.1.0.0/16`

Never store passwords, access keys or private keys in this documentation.

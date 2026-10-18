# SecureNet AWS — Resource Reference

## AWS Region

```text
us-east-1
```

## VPC

```text
Name: Secure-Network-VPC
CIDR: 10.0.0.0/16
```

## Subnets

### Public

```text
10.0.1.0/24
10.0.2.0/24
```

### Private Application

```text
10.0.11.0/24
10.0.12.0/24
```

### Private Database

```text
10.0.21.0/24
10.0.22.0/24
```

## EC2

```text
10.0.11.131
10.0.12.251
```

Application:

```text
Flask + Gunicorn
Port: 5000
Service: contact-api
```

## ALB

```text
contactform-ALB-1366953573.us-east-1.elb.amazonaws.com
```

Target port:

```text
5000
```

Health check:

```text
/health
```

## RDS

```text
Engine: MySQL
Database: securenet
Port: 3306
Table: contact_messages
```

## S3

```text
secure-network-origin-123
```

## CloudFront

```text
Distribution ID:
E1YUP14VLB6ENI
```

## SNS

```text
SecureNet-Admin-Notifications
```

## Systems Manager VPC Endpoints

```text
com.amazonaws.us-east-1.ssm
com.amazonaws.us-east-1.ssmmessages
```

## Transit Gateway Networks

```text
Main VPC:
10.0.0.0/16

Connected VPC:
10.1.0.0/16
```

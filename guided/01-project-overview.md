# 01 — Project Overview

## Objective

Build a secure AWS contact form application using a multi-tier architecture.

The application separates:

1. Frontend
2. Application layer
3. Database layer

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
EC2 Flask Backend
   |
RDS MySQL
   |
SNS Notification
```

## Why this architecture?

The frontend is separated from the backend.

The backend is located inside private application subnets.

The database is located inside private database subnets.

The ALB is responsible for receiving application traffic and distributing it across the EC2 instances.

This improves availability and provides a clear security boundary between the different layers.

## Availability

Two Availability Zones are used.

Application EC2 instances are distributed across:

```text
us-east-1a
us-east-1b
```

This reduces dependency on a single Availability Zone.

## Security

The architecture follows defense-in-depth:

```text
CloudFront
+
WAF
+
Security Groups
+
Private Subnets
+
Systems Manager
+
VPC Endpoints
+
RDS Isolation
+
Flow Logs
+
CloudWatch
```
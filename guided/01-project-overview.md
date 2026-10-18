# 01 — Project Overview

## Objective

Build a secure AWS contact form using a multi-tier architecture.

The application is divided into:

1. Frontend
2. Application layer
3. Database layer

## Request Flow

```text
User
 |
 v
CloudFront
 |
 v
Frontend
 |
 v
ALB
 |
 v
EC2 Flask Backend
 |
 +----> RDS MySQL
 |
 +----> SNS
          |
          v
       Administrator
```

## Why this design?

The frontend, application and database are separated.

The backend is private and receives traffic through the ALB.

The database is private and accepts connections only from the application layer.

Two Availability Zones are used for the application tier.

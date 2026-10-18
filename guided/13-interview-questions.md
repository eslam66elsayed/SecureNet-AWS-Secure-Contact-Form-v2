# 13 — Interview Questions

## Why VPC?

To isolate and control the application's network.

## Why multiple subnets?

To separate public, application and database layers and improve availability across Availability Zones.

## Why private EC2?

The backend does not need direct Internet access. The ALB receives user traffic and forwards it to EC2.

## Why ALB?

For load balancing, health checks and high availability.

## Why `/health`?

The ALB uses it to determine whether an EC2 target is healthy.

## Why RDS?

RDS provides a managed relational database instead of manually managing MySQL on EC2.

## Why private RDS?

To prevent direct Internet access to the database.

## Why only EC2 → RDS on 3306?

Because only the backend needs database access. This follows least privilege.

## Why Systems Manager?

To manage private EC2 instances without exposing SSH.

## What is PrivateLink?

PrivateLink provides private connectivity to supported AWS services through interface VPC endpoints. In this project it is used for Systems Manager endpoints.

## Why S3 Gateway Endpoint?

To provide private access from the VPC to S3 without requiring a public Internet route.

## Why CloudFront?

For CDN delivery, HTTPS, caching and WAF integration.

## WAF vs Shield?

WAF operates at the web request/application layer. Shield provides DDoS protection.

## Why SNS?

To notify the administrator after a successful contact submission.

## Why commit RDS before SNS?

So a notification failure does not cause a successful database submission to be lost.

## Why environment variables?

To avoid hardcoding configuration and secrets.

## Why Gunicorn?

Flask's built-in server is for development. Gunicorn is a production WSGI server.

## Why systemd?

To manage the application as a Linux service and start it automatically.

## What happens if one EC2 fails?

The ALB health check detects the unhealthy target and stops routing traffic to it.

## Why Flow Logs?

For network visibility, troubleshooting and security investigations.

## Why Athena?

To query Flow Logs stored in S3 using SQL.

## Why CloudWatch?

For monitoring metrics and creating alarms.

## Why Transit Gateway?

For centralized connectivity between multiple VPCs.

## Most important security principle?

Least privilege: each component should have only the network and AWS permissions it needs.

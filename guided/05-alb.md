# 05 — Application Load Balancer

## Target Group

Create an Instance target group.

```text
Protocol: HTTP
Port: 5000
Health Check Path: /health
```

Register both EC2 instances.

## ALB

Create an Internet-facing Application Load Balancer.

Use the two public subnets:

```text
us-east-1a
us-east-1b
```

Attach the ALB security group.

Forward traffic to the target group.

## Verify

Both targets should be:

```text
Healthy
```

Test:

```bash
curl http://<ALB-DNS>/health
```

ALB provides load balancing, health checks and higher availability.

# 05 — Application Load Balancer

## Create Target Group

Navigate to:

```text
EC2
→ Target Groups
→ Create target group
```

Configuration:

```text
Target type:
Instances

Protocol:
HTTP

Port:
5000
```

Health check:

```text
Protocol: HTTP
Path: /health
Port: traffic port
```

Register both EC2 instances.

## Create ALB

Create an Internet-facing Application Load Balancer.

Use the two public subnets:

```text
us-east-1a
us-east-1b
```

Attach the ALB security group.

Forward traffic to the target group.

## Verify Health

Both EC2 targets should become:

```text
Healthy
```

Test:

```bash
curl http://<ALB-DNS>/health
```

Expected:

```json
{
  "status": "healthy"
}
```

## Why ALB?

ALB provides:

- Load balancing
- Health checks
- High availability
- Automatic traffic distribution
- Integration with AWS security services
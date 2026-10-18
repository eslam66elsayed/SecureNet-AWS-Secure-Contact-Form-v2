# 09 — Flow Logs, Athena and CloudWatch

## VPC Flow Logs

Flow Logs provide network traffic visibility.

Useful fields include:

```text
Source
Destination
Port
Protocol
Accept / Reject
```

Logs are delivered to S3.

## Athena

Athena can query logs directly from S3.

Example:

```sql
SELECT *
FROM flow_logs
LIMIT 20;
```

This is useful for troubleshooting rejected traffic and investigating network behavior.

## CloudWatch

Monitor:

```text
EC2 CPUUtilization
ALB RequestCount
ALB HTTPCode_ELB_5XX_Count
ALB TargetResponseTime
RDS CPUUtilization
RDS DatabaseConnections
```

Create alarms for important thresholds, such as sustained high EC2 CPU utilization.

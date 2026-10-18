# 12 — Testing and Troubleshooting

## 1. Test Flask Locally

On EC2:

```bash
curl http://127.0.0.1:5000/health
```

Expected:

```text
200 OK
```

## 2. Test ALB

```bash
curl http://<ALB-DNS>/health
```

Expected:

```text
200 OK
```

## 3. Check Target Health

AWS Console:

```text
EC2
→ Target Groups
→ Targets
```

Both targets should be:

```text
Healthy
```

## 4. Check Service

```bash
sudo systemctl status contact-api --no-pager
```

If stopped:

```bash
sudo systemctl restart contact-api
```

## 5. Check Port

```bash
sudo ss -lntp | grep 5000
```

The application should listen on:

```text
0.0.0.0:5000
```

## 6. Test RDS Connectivity

From EC2, test the RDS endpoint and port 3306.

Example:

```bash
nc -zv <RDS-ENDPOINT> 3306
```

## 7. Check Security Groups

Verify:

```text
ALB → EC2 : 5000
EC2 → RDS : 3306
```

## 8. Check Session Manager

If the instance does not appear in Session Manager:

- Verify IAM role.
- Verify SSM Agent.
- Verify VPC endpoints.
- Verify endpoint security groups.
- Verify DNS.
- Verify route tables.

## 9. Check Application Logs

```bash
sudo journalctl -u contact-api -n 100 --no-pager
```

Follow logs:

```bash
sudo journalctl -u contact-api -f
```

## 10. Common Troubleshooting Flow

Always troubleshoot from the bottom layer upward:

```text
VPC
 ↓
Subnet
 ↓
Route Table
 ↓
Security Group
 ↓
EC2
 ↓
Application
 ↓
ALB
 ↓
CloudFront
 ↓
Frontend
```

This prevents random configuration changes.
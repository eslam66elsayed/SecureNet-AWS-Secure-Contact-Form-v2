# 12 — Testing and Troubleshooting

## Flask

```bash
curl http://127.0.0.1:5000/health
```

## ALB

```bash
curl http://<ALB-DNS>/health
```

## Target Health

EC2 → Target Groups → Targets

Both targets should be Healthy.

## Service

```bash
sudo systemctl status contact-api --no-pager
sudo systemctl restart contact-api
```

## Port

```bash
sudo ss -lntp | grep 5000
```

The application should listen on `0.0.0.0:5000`.

## RDS Connectivity

```bash
nc -zv <RDS-ENDPOINT> 3306
```

## Logs

```bash
sudo journalctl -u contact-api -n 100 --no-pager
sudo journalctl -u contact-api -f
```

## Troubleshooting Order

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

Always troubleshoot layer by layer instead of changing random configurations.

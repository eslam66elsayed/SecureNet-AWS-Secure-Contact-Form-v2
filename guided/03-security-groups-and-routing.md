# 03 — Security Groups and Routing

## ALB Security Group

The ALB receives web traffic from users.

Required ports:

```text
HTTP 80
HTTPS 443
```

The ALB forwards application traffic to EC2 on:

```text
TCP 5000
```

## EC2 Security Group

EC2 should allow:

```text
TCP 5000
Source: ALB Security Group
```

The backend should not be directly accessible from the Internet.

## RDS Security Group

RDS MySQL uses:

```text
TCP 3306
```

Source:

```text
EC2 Security Group
```

This means only the application servers can connect to the database.

## Why use Security Group references?

Instead of allowing an IP range such as:

```text
0.0.0.0/0
```

the database trusts the application security group.

This is more secure and follows least privilege.

## Routing

Public subnets:

```text
0.0.0.0/0 → Internet Gateway
```

Private application and database resources do not receive direct Internet access through an Internet Gateway route.

AWS service access is provided through VPC endpoints where configured.
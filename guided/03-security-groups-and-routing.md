# 03 — Security Groups and Routing

## ALB Security Group

Allow the required HTTP/HTTPS traffic from users.

The ALB forwards application traffic to EC2 on TCP `5000`.

## EC2 Security Group

Allow:

```text
TCP 5000
Source: ALB Security Group
```

Do not expose the application directly to the Internet.

## RDS Security Group

Allow:

```text
TCP 3306
Source: EC2 Security Group
```

Do not allow `0.0.0.0/0` to MySQL.

## Public Route Table

```text
10.0.0.0/16 -> local
0.0.0.0/0   -> Internet Gateway
```

Private application and database resources are not directly exposed through an Internet Gateway.

Security Group references are preferred over broad CIDR rules where possible.

# 06 — RDS MySQL Configuration

## DB Subnet Group

Use:

```text
10.0.21.0/24
10.0.22.0/24
```

## Database

```text
Engine: MySQL
Database: securenet
Port: 3306
```

The database must not be publicly accessible.

## Security Group

Allow:

```text
TCP 3306
Source: EC2 Security Group
```

The main table is:

```text
contact_messages
```

Typical fields:

```text
id
name
email
message
created_at
```

The user never connects directly to RDS.

Request flow:

```text
CloudFront → ALB → EC2 → RDS
```

# 06 — RDS MySQL Configuration

## Create DB Subnet Group

Use:

```text
10.0.21.0/24
10.0.22.0/24
```

These are the private database subnets.

## Create RDS

Engine:

```text
MySQL
```

Database:

```text
securenet
```

Port:

```text
3306
```

The database should not be publicly accessible.

## Security Group

Allow:

```text
TCP 3306
Source: EC2 Security Group
```

Do not allow:

```text
0.0.0.0/0
```

## Database Table

The application stores contact messages in:

```text
contact_messages
```

Typical fields include:

```text
id
name
email
message
created_at
```

## Connection Flow

```text
User
 ↓
CloudFront
 ↓
ALB
 ↓
EC2
 ↓
RDS
```

The user never connects directly to RDS.
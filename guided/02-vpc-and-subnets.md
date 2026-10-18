# 02 — VPC and Subnets Configuration

## Create VPC

Open:

```text
AWS Console
→ VPC
→ Your VPCs
→ Create VPC
```

Configuration:

```text
Name:
Secure-Network-VPC

IPv4 CIDR:
10.0.0.0/16
```

## Create Public Subnets

Create two subnets.

### Subnet 1

```text
Name: Public-Subnet-1
AZ: us-east-1a
CIDR: 10.0.1.0/24
```

### Subnet 2

```text
Name: Public-Subnet-2
AZ: us-east-1b
CIDR: 10.0.2.0/24
```

## Create Private Application Subnets

### Subnet 1

```text
Name: Private-App-Subnet-1
AZ: us-east-1a
CIDR: 10.0.11.0/24
```

### Subnet 2

```text
Name: Private-App-Subnet-2
AZ: us-east-1b
CIDR: 10.0.12.0/24
```

## Create Private Database Subnets

### Subnet 1

```text
Name: Private-DB-Subnet-1
AZ: us-east-1a
CIDR: 10.0.21.0/24
```

### Subnet 2

```text
Name: Private-DB-Subnet-2
AZ: us-east-1b
CIDR: 10.0.22.0/24
```

## Why multiple subnet types?

Public subnets are used for internet-facing infrastructure.

Private application subnets protect backend servers from direct Internet access.

Private database subnets protect the database from direct access.

This creates a layered architecture.
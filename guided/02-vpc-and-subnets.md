# 02 — VPC and Subnets Configuration

## Create VPC

AWS Console:
VPC → Your VPCs → Create VPC

Use:

```text
Name: Secure-Network-VPC
IPv4 CIDR: 10.0.0.0/16
```

## Public Subnets

```text
Public-Subnet-1
AZ: us-east-1a
CIDR: 10.0.1.0/24

Public-Subnet-2
AZ: us-east-1b
CIDR: 10.0.2.0/24
```

## Private Application Subnets

```text
Private-App-Subnet-1
AZ: us-east-1a
CIDR: 10.0.11.0/24

Private-App-Subnet-2
AZ: us-east-1b
CIDR: 10.0.12.0/24
```

## Private Database Subnets

```text
Private-DB-Subnet-1
AZ: us-east-1a
CIDR: 10.0.21.0/24

Private-DB-Subnet-2
AZ: us-east-1b
CIDR: 10.0.22.0/24
```

Public subnets are for internet-facing infrastructure.

Private application subnets protect the backend.

Private database subnets protect RDS.

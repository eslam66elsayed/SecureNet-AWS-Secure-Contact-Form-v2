# 08 — Systems Manager and VPC Endpoints

## Systems Manager

Use Session Manager to access private EC2 instances.

This avoids exposing SSH to the Internet.

The EC2 instance requires an IAM role with the required Systems Manager permissions, commonly including:

`AmazonSSMManagedInstanceCore`

## Interface Endpoints

Configured:

```text
com.amazonaws.us-east-1.ssm
com.amazonaws.us-east-1.ssmmessages
```

## S3 Gateway Endpoint

An S3 Gateway Endpoint is also configured.

VPC endpoints provide private access to supported AWS services.

## Test Session

From Session Manager:

```bash
hostname
sudo systemctl status contact-api --no-pager
```

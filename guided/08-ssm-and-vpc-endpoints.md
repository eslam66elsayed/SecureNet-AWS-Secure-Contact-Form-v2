# 08 — Systems Manager and VPC Endpoints

## Why Systems Manager?

The EC2 instances are private.

Instead of opening SSH to the Internet, Systems Manager Session Manager is used.

This avoids exposing port:

```text
22
```

## Session Manager

Navigate:

```text
AWS Systems Manager
→ Session Manager
→ Start session
```

Select the EC2 instance.

## Required IAM Role

The EC2 instance needs an IAM role allowing Systems Manager functionality.

The managed policy commonly used is:

```text
AmazonSSMManagedInstanceCore
```

## VPC Endpoints

Configured endpoints include:

```text
com.amazonaws.us-east-1.ssm
com.amazonaws.us-east-1.ssmmessages
```

An S3 Gateway Endpoint is also configured.

## Why VPC Endpoints?

They allow private communication with supported AWS services without requiring Internet access.

This is particularly useful for private EC2 instances.

## Test Session

After connecting through Session Manager:

```bash
hostname
```

Then test:

```bash
sudo systemctl status contact-api --no-pager
```
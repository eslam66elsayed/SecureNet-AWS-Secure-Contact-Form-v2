# 11 — Transit Gateway

## Objective

Transit Gateway is used to demonstrate centralized connectivity between multiple VPCs.

## Networks

Main VPC:

```text
10.0.0.0/16
```

Second VPC:

```text
10.1.0.0/16
```

## Architecture

```text
VPC 10.0.0.0/16
        |
        |
Transit Gateway
        |
        |
VPC 10.1.0.0/16
```

## Why Transit Gateway?

Without Transit Gateway, multiple VPCs can become difficult to manage because each VPC may require individual connections.

Transit Gateway provides a centralized routing point.

## Routing

Both VPC route tables must contain the required routes toward the Transit Gateway.

Example:

```text
10.1.0.0/16 → Transit Gateway
```

and in the second VPC:

```text
10.0.0.0/16 → Transit Gateway
```

## Important

Transit Gateway does not automatically make resources reachable.

Security Groups, Network ACLs, and route tables must still allow the traffic.
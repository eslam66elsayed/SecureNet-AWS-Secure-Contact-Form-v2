# 11 — Transit Gateway

## Networks

Main VPC:

`10.0.0.0/16`

Connected VPC:

`10.1.0.0/16`

## Architecture

```text
VPC 10.0.0.0/16
        |
Transit Gateway
        |
VPC 10.1.0.0/16
```

Transit Gateway provides centralized connectivity between VPCs.

Required routes must point the opposite VPC CIDR toward the Transit Gateway.

Example:

```text
10.1.0.0/16 → Transit Gateway
```

and:

```text
10.0.0.0/16 → Transit Gateway
```

Transit Gateway does not bypass Security Groups or Network ACLs. Routing and security controls must both allow the traffic.

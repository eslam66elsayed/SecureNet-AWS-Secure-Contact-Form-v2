# 07 — S3, CloudFront and WAF

## S3

Create the frontend bucket.

Example:

```text
secure-network-origin-123
```

Upload:

```text
index.html
style.css
script.js
```

The S3 bucket should not be treated as the public entry point.

## CloudFront

Create a CloudFront distribution using the S3 bucket as the origin.

CloudFront provides:

- HTTPS
- CDN
- Caching
- Global edge delivery
- WAF integration

Distribution:

```text
E1YUP14VLB6ENI
```

## Frontend API

The frontend sends requests to:

```javascript
fetch("/api/contact")
```

The API behavior is routed through the configured application origin.

## WAF

Attach AWS WAF to CloudFront.

Recommended protections:

```text
AWS Managed Rules
Common Rule Set
Known Bad Inputs
SQL Injection protection
```

Rate-based protection can also be used to reduce abusive request rates.

## Why WAF?

CloudFront protects delivery and WAF inspects HTTP requests for malicious patterns.

This provides an additional security layer before requests reach the application.
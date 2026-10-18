# 07 — S3, CloudFront and WAF

## S3

Frontend bucket:

`secure-network-origin-123`

Upload:

```text
index.html
style.css
script.js
```

S3 is used as the frontend origin.

## CloudFront

Distribution ID:

`E1YUP14VLB6ENI`

CloudFront provides HTTPS, CDN delivery, caching and WAF integration.

## WAF

Associate AWS WAF with CloudFront.

Use appropriate managed protections such as common web attack rules and rate-based protection.

WAF helps protect against common malicious web requests.

## Shield

AWS Shield provides DDoS protection.

CloudFront and AWS infrastructure provide baseline protection, while Shield Advanced can add additional capabilities when required.

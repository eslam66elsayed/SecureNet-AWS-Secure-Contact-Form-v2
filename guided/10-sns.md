# 10 — SNS Notification

## Topic

`SecureNet-Admin-Notifications`

SNS sends an administrator notification after a successful contact form submission.

## Application Flow

```text
POST /api/contact
        |
Input validation
        |
Insert into RDS
        |
Commit transaction
        |
Publish SNS
        |
Administrator notification
```

The database transaction is committed before publishing SNS.

Therefore, a temporary SNS failure does not remove a successfully stored contact message.

## Test

1. Submit the form.
2. Verify the API returns success.
3. Verify the message exists in RDS.
4. Verify the SNS notification.

SNS is different from SES. SNS is used here for publish/subscribe notifications, while SES is primarily an email sending service.

# 10 — SNS Notification

## SNS Topic

Topic:

```text
SecureNet-Admin-Notifications
```

The topic is used for administrator notifications.

## Application Flow

When a user submits the contact form:

```text
POST /api/contact
        |
        v
Input validation
        |
        v
Insert into RDS
        |
        v
Commit transaction
        |
        v
Publish SNS message
```

## Important Design Decision

The database transaction is committed before publishing the SNS notification.

This means the contact message remains stored even if SNS temporarily fails.

The notification system should not cause a successful database submission to be lost.

## Test

Submit the contact form and verify:

1. The API returns success.
2. The message exists in RDS.
3. The SNS notification is received.

## SES vs SNS

SNS is being used for administrator notifications.

It is different from SES.

SNS is a publish/subscribe notification service, while SES is designed primarily for sending email.
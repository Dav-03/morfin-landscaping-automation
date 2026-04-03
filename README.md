# Morfin Landscaping Automation

Automated client scheduling and payment reminder system 
built for a small landscaping business using Python and AWS.

## Architecture
EventBridge -> Lambda (Scheduler) -> S3 -> Email Notification
EventBridge -> Lambda (Payments)  -> S3 -> Email Notification

## Services Used
- AWS Lambda: runs scheduling and payment logic
- Amazon S3: stores client data (Clients.csv)
- AWS Secrets Manager: securely stores email credentials
- Amazon EventBridge: triggers both Lambdas every 2 weeks

## How It Works
1. EventBridge triggers both Lambda functions on a schedule
2. Each Lambda reads client data from S3
3. Scheduler checks which clients are scheduled for today
4. Payments checks which clients have overdue payments
5. Notifications are sent via email gateway

## Setup
1. Clone the repository
2. Create an S3 bucket and upload Clients.csv
3. Store email credentials in AWS Secrets Manager
4. Deploy each .py file as a Lambda function
5. Set up EventBridge trigger with rate of 14 days

## Project Structure
- src/Scheduler.py: identifies today's scheduled clients
- src/Payments.py: identifies clients behind on payments
- src/Notifier.py: handles sending notifications
- src/emailConfig.py: fetches credentials from Secrets Manager

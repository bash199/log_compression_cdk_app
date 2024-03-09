# Log File Upload and Auto-Compression System

Aa solution using AWS CDK to facilitate log file uploads, auto-compression, and
storage.
It include an API Gateway and Lambda to accept log file content and store in S3 Bucket, another Lambda function to compress the log file, and S3 buckets for both uncompressed and
compressed log files.

## Components

-  API Gateway
-  Lambda Functions
-  S3 Buckets

## Purpose of Each Component

-  API Gateway: Receives log file content via HTTP POST requests.

-  Lambda Function (Process): Processes the log file content and stores it in an S3 bucket.

-  Lambda Function (Compress): Compresses the log file and stores it in another S3 bucket.

-  S3 Buckets: One for storing uncompressed log files and another for storing compressed log files.

## Usage

-  First Configure AWS CLI .

-  grant the needed permissions (AdministratorAccess) if not using root.

-  Bootstarp your cdk toolkit (run cdk bootsrapt account-id/region)

-  Clone the repository.

-  Install dependencies (requirements.txt).

-  Deploy the CDK stack (cdk deploy).

-  Use the provided API Gateway endpoint to send HTTP POST requests with log file content.

## Testing

-  Install testing dependencies (requirements-dev.txt).
-  Run the tests (pytest).

Enjoy!

# AWS Lambda Function S3 Copy Python example

This folder contains an AWS Lambda Function example in Python on AWS (Amazon Web Services).

It handles an AWS Lambda function that copies an object when it appears in a S3 bucket to another S3 bucket using the Client API (low-level) of Boto 3.

## Requirements

* You must have an [Amazon Web Services (AWS)](http://aws.amazon.com/) account.

* The code was written for Python 3 and AWS SDK for Python (Boto 3).

* This example uses Client API (low-level) of Boto 3.

* The AWS Lambda execution environment include SDK for Python (Boto 3).

## Using the code

* You can select the destination bucket name changing the value of `DESTINATION_BUCKET` variable in the code.

* Access the AWS console.

* Create a S3 bucket for the source and another S3 bucket for the target.

* Create an IAM Policy: ex. `Policy-VM-buckets`

  Content of the IAM policy:

  ```bash
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "s3:GetObject"
              ],
              "Resource": [
                  "arn:aws:s3:::sourcevm/*"
              ]
          },
          {
              "Effect": "Allow",
              "Action": [
                  "s3:PutObject"
              ],
              "Resource": [
                  "arn:aws:s3:::targetvm/*"
              ]
          },
          {
              "Sid": "Stmt1430872844000",
              "Effect": "Allow",
              "Action": [
                  "cloudwatch:*"
              ],
              "Resource": [
                  "*"
              ]
          },
          {
              "Sid": "Stmt1430872852000",
              "Effect": "Allow",
              "Action": [
                  "logs:*"
              ],
              "Resource": [
                  "*"
              ]
          }
      ]
  }
  ```

* Create a role: `Role-VM-buckets`.

  This role uses the policy `Policy-VM-buckets`

* Create an AWS lambda function.
  * Name: `<LAMBDA_NAME>`
  * Runtime: `Python 3.6`
  * Handler: `lambda_function.lambda_handler`
  * Role: `Role-VM-buckets`
  * The triggers:
    * `S3`
      * Bucket: `<BUCKET_NAME>`
      * Event type: `ObjectCreated`
      * Enable trigger: `Yes`
  * The resources that the function's role has access to:
    * `Amazon CloudWatch`
    * `Amazon CloudWatch Logs`
    * `Amazon S3`
      * Lambda obtained information from the policy statements: `Managed policy Policy-VM-buckets`
  * Basic Settings for the lambda function:
    * Memory (MB): `1024`
    * Timeout: `10 sec`

* Write the code.

  The content of `lambda_function.py` file.

* Save the Lambda function.

  It deploys the Lambda function.

* Test the function:

  Copy a file in the source S3 bucket.

  The object from the source S3 bucket should be copied to the target S3 bucket.

# AWS Lambda Function S3 Event Python example

This folder contains an AWS Lambda Function example in Python on AWS (Amazon Web Services).

It handles an AWS Lambda function that sends information to the log about an object when it appears in a S3 bucket.

## Requirements

* You must have an [Amazon Web Services (AWS)](http://aws.amazon.com/) account.

* The code was written for Python 3.

## Using the code

* Access the AWS console.

* Create a S3 bucket.

* Create an AWS lambda function.
  * Name: `<LAMBDA_NAME>`
  * Runtime: `Python 3.6`
  * Handler: `lambda_function.lambda_handler`
  * Role: `lambda-basic-execution`
  * The triggers:
    * `S3`
      * Bucket: `<BUCKET_NAME>`
      * Event type: `ObjectCreated`
      * Enable trigger: `Yes`
  * The resources that the function's role has access to:
    * `Amazon CloudWatch Logs`
  * Basic Settings for the lambda function:
    * Memory (MB): `128`
    * Timeout: `3 sec`

* Write the code.

  The content of `lambda_function.py` file.

* Save the Lambda function.

  It deploys the Lambda function.

* Test the function:

  Copy a file in the source S3 bucket.

  You should see the next message in the log:

  ```bash
  "Input: <LAMBDA_INPUT>"
  "Bucket: <BUCKET_NAME>"
  "Object: <OBJECT_NAME>"
  ```
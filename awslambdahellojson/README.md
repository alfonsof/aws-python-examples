# AWS Lambda Function Hello World JSON Python example

This folder contains an AWS Lambda Function example in Python on AWS (Amazon Web Services).

It handles a simple AWS Lambda function that shows the content (JSON) of the call to the lambda function and returns a message including this content.

## Requirements

* You must have an [Amazon Web Services (AWS)](http://aws.amazon.com/) account.

* The code was written for Python 3.

## Using the code

* Access the AWS console.

* Select AWS Lambda in the services menu.

* Create an AWS lambda function.
  * Name: `<LAMBDA_NAME>`
  * Runtime: `Python 3.8`
  * Handler: `lambda_function.lambda_handler`
  * Role: `lambda-basic-execution`
  * Runtime Settings for the lambda function:
    * Memory (MB): `128`
    * Timeout: `3 sec`
  * The resources that the function's role has access to:
    * `Amazon CloudWatch Logs`
  * The triggers:
    * `Nothing`

* Write the code.

  The content of `lambda_function.py` file.

* Save the Lambda function.

  It deploys the Lambda function.

* Create and configure a Test event.

  Input JSON file content:

  ```bash
  {
    "first_name": "Peter",
    "last_name": "Parker"
  }
  ```

* Run the code.

  Run the code in an AWS lambda function using the test button.

* Test the AWS Lambda function.

  You should see the next message in the log:

  ```bash
  {
    "message": "Hello Peter Parker!"
  }
  ```

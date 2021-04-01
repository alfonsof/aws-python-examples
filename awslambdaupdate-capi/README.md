# AWS Lambda Function Update Python example

This folder contains a Python application example that handles Lambda functions on AWS (Amazon Web Services).

Update an AWS Lambda function using the Client API (low-level) of Boto 3.

## Requirements

* You must have an [Amazon Web Services (AWS)](http://aws.amazon.com/) account.

* The code was written for:

  * Python 3
  * AWS SDK for Python (Boto3)

* This example uses Client API (low-level) of Boto 3.

* Install the AWS SDK for Python (Boto3).

  Install the latest Boto 3 release via pip:

  ```bash
  pip install boto3
  ```

## Using the code

* Configure your AWS access keys.

  **Important:** For security, it is strongly recommend that you use IAM users instead of the root account for AWS access.

  When you initialize a new service client without supplying any arguments, the AWS SDK for Java attempts to find AWS credentials by using the default credential provider chain.

  Setting your credentials for use by the AWS SDK for Java can be done in a number of ways, but here are the recommended approaches:

  * The default credential profiles file
  
    Set credentials in the AWS credentials profile file on your local system, located at:

    `~/.aws/credentials` on Linux, macOS, or Unix

    `C:\Users\USERNAME\.aws\credentials` on Windows

    This file should contain lines in the following format:

    ```bash
    [default]
    aws_access_key_id = <your_access_key_id>
    aws_secret_access_key = <your_secret_access_key>
    ```
    Substitute your own AWS credentials values for the values `<your_access_key_id>` and `<your_secret_access_key>`.

  * Environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
  
    Set the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables.

    To set these variables on Linux, macOS, or Unix, use `export`:

    ```bash
    export AWS_ACCESS_KEY_ID=<your_access_key_id>
    export AWS_SECRET_ACCESS_KEY=<your_secret_access_key>
    ```

    To set these variables on Windows, use `set`:

    ```bash
    set AWS_ACCESS_KEY_ID=<your_access_key_id>
    set AWS_SECRET_ACCESS_KEY=<your_secret_access_key>
    ```

* The AWS Lambda function to update must already exist.

  You can use the AWS Lambda Function Hello World JSON Java example: [awslambdahellojson](/awslambdahellojson).

* You need a `.py` file where the code of the Lambda function is located.

  You can use the code obtained from the AWS Lambda Function Hello World JSON Java example: [awslambdahellojson](/awslambdahellojson).

  This application compresses the `.py` file in a `ZIP` file to deploy.

* You can select the AWS region of the Lambda function changing the value of `REGION` variable in the code.

* You have to create an AWS role that has Lambda permissions.

* Run the code.

  You must provide 4 parameters:
  
  * `<FUNCTION_NAME>`    = Lambda function name
  * `<FUNCTION_FILE>`    = The path to the `.py` file where the code of the Lambda function is located
  * `<FUNCTION_ROLE>`    = The role ARN that has Lambda permissions
  * `<FUNCTION_HANDLER>` = The fully qualifed method name (Ex: lambda_function.lambda_handler)

  Run application:

  ```bash
  python lambdaupdate.py lambda-name lambda-file lambda-role lambda-handler
  ```

  You must use as a function role the ARN.

  Ex.: `arn:aws:iam::123456789012:role/service-role/lambda-basic-execution`

* Test the application.

  You should see the response of the Lambda function.

  For example:

  * `Updating function ...`
  * `Updated function "FunctionName"`

  And the Lambda function updated.
  
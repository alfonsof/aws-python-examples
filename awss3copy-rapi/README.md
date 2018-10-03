# AWS S3 Copy Python example

This folder contains a Python application example that handles S3 buckets on AWS (Amazon Web Services).

Copy an object from a S3 bucket to another S3 bucket using the Resource API (high-level) of Boto 3.

## Requirements

* You must have an [Amazon Web Services (AWS)](http://aws.amazon.com/) account.

* The code was written for Python 3 and AWS SDK for Python (Boto3).

* This example uses Resource API (high-level) of Boto 3.

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

* Create a S3 bucket for the source and another S3 bucket for the target.

* Copy a file to the source S3 bucket.

* Run the code.

  You must provide 3 parameters:
  
  * `<SOURCE_BUCKET>`      = Source bucket name
  * `<SOURCE_FILE>`        = Source file name
  * `<DESTINATION_BUCKET>` = Destination bucket name

  Run application:

  ```bash
  python s3copy.py bucket-name source-bucket source-file destination-bucket
  ```

* Test the application.

  The object from the source S3 bucket should be copied to the target S3 bucket.

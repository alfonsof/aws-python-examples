# AWS EC2 Instances Python example

This folder contains a Python application example that handles EC2 instances on AWS (Amazon Web Services).

Manage Amazon EC2 Instances using the Client API (low-level) of Boto 3.

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

  * The default credential profiles file.
  
    Set credentials in the AWS credentials profile file on your local system, located at:

    * `~/.aws/credentials` on Linux, macOS, or Unix.

    * `C:\Users\USERNAME\.aws\credentials` on Windows.

    This file should contain lines in the following format:

    ```bash
    [default]
    aws_access_key_id = <YOUR_ACCESS_KEY_ID>
    aws_secret_access_key = <YOUR_SECRET_ACCESS_KEY>
    ```
    Replace the values of `<YOUR_ACCESS_KEY_ID>` and `<YOUR_SECRET_ACCESS_KEY>` by your AWS credentials.

  * Environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.
  
    Set the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables.

    To set these variables on Linux, macOS, or Unix, use `export`:

    ```bash
    export AWS_ACCESS_KEY_ID=<YOUR_ACCESS_KEY_ID>
    export AWS_SECRET_ACCESS_KEY=<YOUR_SECRET_ACCESS_KEY>
    ```

    To set these variables on Windows, use `set`:

    ```bash
    set AWS_ACCESS_KEY_ID=<YOUR_ACCESS_KEY_ID>
    set AWS_SECRET_ACCESS_KEY=<YOUR_SECRET_ACCESS_KEY>
    ```

    Replace the values of `<YOUR_ACCESS_KEY_ID>` and `<YOUR_SECRET_ACCESS_KEY>` by your AWS credentials.

* Run the code.

  Run application:

  ```bash
  python ec2instances.py
  ```

  You can select an option in the menu in order to run every command:

  * 1 = Describe all instances
  * 2 = Run new instance
  * 3 = Describe instance
  * 4 = Start instance
  * 5 = Stop instance
  * 6 = Reboot instance
  * 7 = Terminate instance

* Test the application.

  You should see the new instance and modification of states with the AWS console.

#!/usr/bin/python
# -*- coding: utf-8 -*-
# lambdaupdate.py
# It is an example that handles Lambda functions on AWS.
# It uses Client API (low-level) of Boto3.
# Update a Lambda function.
# You must provide 1 parameter:
# FUNCTION_NAME      = Lambda function name
# FUNCTION_FILE      = The path to the .py file where the code of the Lambda function is located
# FUNCTION_ROLE      = The role ARN that has Lambda permissions
# FUNCTION_HANDLER   = The fully qualifed method name (Ex: lambda_function.lambda_handler)

import sys
import io
import zipfile
import boto3
import botocore

def create_lambda_deployment_package(function_file_name):
    # Creates a Lambda deployment package in ZIP format in an in-memory buffer.
    # This buffer can be passed directly to AWS Lambda when creating the function.
    # Parameters:
    #     function_file_name (string): The name of the file that contains the Lambda handler function.
    # Return:
    #     The deployment package.

    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w') as zipped:
        zipped.write(function_file_name)
    buffer.seek(0)
    return buffer.read()


def main():

    REGION = 'eu-west-1'   # AWS region

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if len(args) < 4:
        print('Not enough parameters.\n'\
              'Proper Usage is: python lambdaupdate.py '\
              '<FUNCTION_NAME> <FUNCTION_FILE<> <FUNCTION_ROLE> <FUNCTION_HANDLER>')
        sys.exit(1)

    function_name = args[0]
    function_file = args[1]
    function_role = args[2]
    function_handler = args[3]

    print('Lambda function name:    ' + function_name)
    print('Lambda function file:    ' + function_file)
    print('Lambda function role:    ' + function_role)
    print('Lambda function handler: ' + function_handler)

    # Create a Lambda Client
    lambda_client = boto3.client('lambda', region_name=REGION)

    # Create Lambda function
    try:
        print('Updating function ...')
        
        deployment_package = create_lambda_deployment_package(function_file)

        # Update Lambda function configuration
        response = lambda_client.update_function_configuration(
                      FunctionName=function_name,
                      Description='Updated by the Lambda Python API',
                      Runtime='python3.8',
                      Role=function_role,
                      Handler=function_handler)

        print('Response (Conf.):')
        print(response)
        function_arn_conf = response['FunctionArn']

        # Update Lambda function code
        response = lambda_client.update_function_code(
                      FunctionName=function_name,
                      ZipFile=deployment_package,
                      Publish=True)

        print('Response (Code):')
        print(response)
        function_arn_code = response['FunctionArn']

        print('\nUpdated function "' + function_name + '"')
        print('The function ARN (Conf.) is ' + function_arn_conf)
        print('The function ARN (Code) is  ' + function_arn_code)

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "AccessDeniedException":
          print("Error: Access Denied!!")
        elif e.response['Error']['Code'] == "ValidationException":
          print("Error: Name Not Valid!!")
        else:
          raise

    return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
    
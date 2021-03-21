#!/usr/bin/python
# -*- coding: utf-8 -*-
# lambdalist.py
# It is an example that handles Lambda functions on AWS.
# It uses Client API (low-level) of Boto3.
# List information of a Lambda function.
# You must provide 1 parameter:
# FUNCTION_NAME      = Lambda function name

import sys
import boto3
import botocore

def main():

    REGION = 'eu-west-1'   # AWS region

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if len(args) < 1:
        print('Not enough parameters.\n'\
              'Proper Usage is: python lambdalist.py <FUNCTION_NAME>')
        sys.exit(1)

    function_name = args[0]
    print('Lambda function name: ' + function_name)

    # Create a Lambda Client
    lambda_client = boto3.client('lambda', region_name=REGION)

    # List lambda function configuration
    try:
        print('Listing function ...')

        config = lambda_client.get_function_configuration(
                        FunctionName=function_name)

        print('Function name: ', config['FunctionName'])
        print('  - ARN: ', config['FunctionArn'])
        print('  - Runtime: ', config['Runtime'])
        print('  - Role: ', config['Role'])
        print('  - Handler: ', config['Handler'])
        print('  - Description: ', config['Description'])
        print('  - Timeout: ', config['Timeout'])
        print('  - MemorySize: ', config['MemorySize'])
        print('  - LastModified: ', config['LastModified'])
        print('  - Description: ', config['Description'])
        print('  - CodeSize: ', config['CodeSize'])
        print('  - Version: ', config['Version'])

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "ResourceNotFoundException":
            print("Error: Function Not Found!!")
        elif e.response['Error']['Code'] == "AccessDeniedException":
            print("Error: Access Denied!!")
        elif e.response['Error']['Code'] == "ValidationException":
            print("Error: Name Not Valid!!")
        else:
            raise

    return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()

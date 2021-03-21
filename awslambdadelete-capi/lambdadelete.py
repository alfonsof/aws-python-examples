#!/usr/bin/python
# -*- coding: utf-8 -*-
# lambdadelete.py
# It is an example that handles Lambda functions on AWS.
# It uses Client API (low-level) of Boto3.
# Delete a Lambda function.
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
              'Proper Usage is: python lambdadelete.py <FUNCTION_NAME>')
        sys.exit(1)

    function_name = args[0]
    print('Lambda function name: ' + function_name)

    # Create a Lambda Client
    lambda_client = boto3.client('lambda', region_name=REGION)

    # Delete Lambda function
    try:
        print('Deleting function ...')

        response = lambda_client.delete_function(
                            FunctionName=function_name)

        print('Response:')
        print(response)
        print('\nDeleted')

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

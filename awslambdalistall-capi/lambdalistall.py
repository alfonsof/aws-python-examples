#!/usr/bin/python
# -*- coding: utf-8 -*-
# lambdalistall.py
# It is an example that handles Lambda functions on AWS.
# It uses Client API (low-level) of Boto3.
# List all Lambda functions and their information.

import sys
import boto3
import botocore

def main():

    REGION = 'eu-west-1'   # AWS region

    # Create a Lambda Client
    lambda_client = boto3.client('lambda', region_name=REGION)

    # List lambda functions
    try:
        print('Listing functions ...')
        list_functions_resp = lambda_client.list_functions()
        for function in list_functions_resp['Functions']:
            print('Function name: ', function['FunctionName'])
            print('  - ARN: ', function['FunctionArn'])
            print('  - Runtime: ', function['Runtime'])
            print('  - Role: ', function['Role'])
            print('  - Handler: ', function['Handler'])
            print('  - Description: ', function['Description'])
            print('  - Timeout: ', function['Timeout'])
            print('  - MemorySize: ', function['MemorySize'])
            print('  - LastModified: ', function['LastModified'])
            print('  - Description: ', function['Description'])
            print('  - CodeSize: ', function['CodeSize'])
            print('  - Version: ', function['Version'])

    except botocore.exceptions.ClientError as e:
        raise

    return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()

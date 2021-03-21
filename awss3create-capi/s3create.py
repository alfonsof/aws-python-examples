#!/usr/bin/python
# -*- coding: utf-8 -*-
# s3create.py
# It is an example that handles S3 buckets on AWS.
# It uses Client API (low-level) of Boto3.
# Create a new S3 bucket.
# You must provide 1 parameter:
# BUCKET_NAME = Name of the bucket

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
              'Proper Usage is: python s3create.py <BUCKET_NAME>')
        sys.exit(1)

    bucket_name = args[0]
    print('Bucket name: ' + bucket_name)

    # Create an S3 Client
    s3_client = boto3.client('s3')

    # Create the bucket object
    try:
        print('Creating bucket ...')
        response = s3_client.create_bucket(ACL='private',
                                          Bucket=bucket_name,
                                          CreateBucketConfiguration={
                                            'LocationConstraint': REGION})
        print(response)
        print('\nCreated')
        print(response['Location'])

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "BucketAlreadyOwnedByYou":
            print("Error: Bucket already created and owned by you!!")
        elif e.response['Error']['Code'] == "BucketAlreadyExists":
            print("Error: Bucket already exist!!")
        elif e.response['Error']['Code'] == "InvalidBucketName":
            print("Error: Invalid Bucket name!!")
        else:
            raise

    return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()

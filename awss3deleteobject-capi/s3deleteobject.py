#!/usr/bin/python
# -*- coding: utf-8 -*-
# s3deleteobject.py
# It is an example that handles S3 buckets on AWS.
# It uses Client API (low-level) of Boto3.
# Delete an object in a S3 bucket.
# You must provide 2 parameters:
# BUCKET_NAME = Name of the bucket
# OBJECT_NAME = Name of the object in the bucket

import sys
import boto3
import botocore

def main():

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if len(args) < 2:
        print('Not enough parameters.\n'\
              'Proper Usage is: python s3deleteobject.py '\
              '<BUCKET_NAME> <OBJECT_NAME>')
        sys.exit(1)

    bucket_name = args[0]
    key_name = args[1]
    print('Bucket name: ' + bucket_name)
    print('Object name: ' + key_name)

    # Create an S3 Client
    s3_client = boto3.client('s3')

    # Delete the bucket object
    try:
        print('Deleting object ...')
        # Delete the object from bucket
        response = s3_client.delete_object(Bucket=bucket_name, Key=key_name)
        print(response)
        print('\nDeleted')

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "AccessDenied":
            print("Error: Access denied!!")
        elif e.response['Error']['Code'] == "InvalidBucketName":
            print("Error: Invalid Bucket name!!")
        elif e.response['Error']['Code'] == "NoSuchBucket":
            print("Error: Bucket does not exist!!")
        elif e.response['Error']['Code'] == "AllAccessDisabled":
            print("Error: You do not have access to the Bucket!!")
        else:
            raise

    return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()

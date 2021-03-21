#!/usr/bin/python
# -*- coding: utf-8 -*-
# s3list.py
# It is an example that handles S3 buckets on AWS.
# It uses Resource API (high-level) of Boto3.
# List information about the objects in a S3 bucket.
# You must provide 1 parameter:
# BUCKET_NAME = Name of the bucket

import sys
import boto3
import botocore

def main():

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if len(args) < 1:
        print('Not enough parameters.\n'\
              'Proper Usage is: python s3list.py <BUCKET_NAME>')
        sys.exit(1)

    bucket_name = args[0]
    print('Bucket name: ' + bucket_name)

    # Instantiate the service resource object
    s3_resource = boto3.resource('s3')

    #  Instantiate the bucket object
    bucket = s3_resource.Bucket(bucket_name)

    print('Listing objects ...')
    # List buckets
    try:
        for s3object in bucket.objects.all():
            print(' - Object: ' + s3object.key)

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "NoSuchBucket":
            print("Error: Bucket does not exist!!")
        elif e.response['Error']['Code'] == "InvalidBucketName":
            print("Error: Invalid Bucket name!!")
        elif e.response['Error']['Code'] == "AllAccessDisabled":
            print("Error: You do not have access to the Bucket!!")
        else:
            raise

    return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()

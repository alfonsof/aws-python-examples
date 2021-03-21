#!/usr/bin/python
# -*- coding: utf-8 -*-
# s3listall.py
# It is an example that handles S3 buckets on AWS.
# It uses Client API (low-level) of Boto3.
# List information about all S3 buckets and the objects they contain.

import sys
import boto3
import botocore

def main():

    # Create an S3 Client
    s3_client = boto3.client('s3')

    print('Listing S3 buckets and objects ...')
    # List buckets
    list_buckets_resp = s3_client.list_buckets()
    for bucket in list_buckets_resp['Buckets']:
        print('* Bucket: ' + bucket['Name'])
        s3objects = s3_client.list_objects_v2(Bucket=bucket['Name'])
        if s3objects['KeyCount'] > 0:
            for s3object in s3objects['Contents']:
                print(' - Object: ' + s3object['Key'])

    return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()

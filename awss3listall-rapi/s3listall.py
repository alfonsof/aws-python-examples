#!/usr/bin/python
# -*- coding: utf-8 -*-
# s3listall.py
# It is an example that handles S3 buckets on AWS.
# It uses Resource API (high-level) of Boto3.
# List information about all S3 buckets and the objetcs they contain.

import sys
import boto3
import botocore

def main():

    # Instantiate the service resource object
    s3_resource = boto3.resource('s3')

    print('Listing S3 buckets and objects ...')
    # List buckets
    for bucket in s3_resource.buckets.all():
        print('* Bucket: ' + bucket.name)
        for s3object in bucket.objects.all():
            print(' - Object: ' + s3object.key)

    return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()

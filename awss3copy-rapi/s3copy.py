#!/usr/bin/python
# -*- coding: utf-8 -*-
# s3copy.py
# It is an example that handles S3 buckets on AWS.
# It uses Resource API (high-level) of Boto3.
# Copy an object from a S3 bucket to another S3 bucket.
# You must provide 3 parameters:
# SOURCE_BUCKET      = Source bucket name
# SOURCE_OBJECT      = Source file name
# DESTINATION_BUCKET = Destination bucket name

import sys
import boto3
import botocore

def main():

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if len(args) < 3:
        print('Not enough parameters.\n'\
              'Proper Usage is: python s3copy.py '\
              '<SOURCE_BUCKET> <SOURCE_OBJECT> <DESTINATION_BUCKET>')
        sys.exit(1)

    source_bucket_name = args[0]
    source_key = args[1]
    destination_bucket_name = args[2]
    destination_key = source_key
    print('From - bucket: ' + source_bucket_name)
    print('From - object: ' + source_key)
    print('To   - bucket: ' + destination_bucket_name)
    print('To   - object: ' + destination_key)

    # Instantiate the service resource object
    s3_resource = boto3.resource('s3')

    # Copy the object
    try:
        print('Copying object ...')
        #  Instantiate the destination bucket
        dest_bucket = s3_resource.Bucket(destination_bucket_name)
        copy_source = {
            'Bucket': source_bucket_name,
            'Key': source_key
          }
        dest_bucket.copy(copy_source, destination_key)
        print('Copied')
  
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("Error: Not Found, problem with the parameters!!")
        elif e.response['Error']['Code'] == "400":
            print("Error: Bad request, problem with the bucket!!")
        elif e.response['Error']['Code'] == "403":
            print("Error: Forbidden, bucket forbidden!!")
        elif e.response['Error']['Code'] == "AccessDenied":
            print("Error: Access denied!!")
        elif e.response['Error']['Code'] == "InvalidBucketName":
           print("Error: Invalid bucket name!!")
        elif e.response['Error']['Code'] == "NoSuchBucket":
            print("Error: No such bucket!!")
        else:
            raise

    return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()

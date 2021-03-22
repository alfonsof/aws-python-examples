# lamdda_function.py
# It handles an AWS Lambda function that moves an object when it appears
# in a S3 bucket to another S3 bucket.
# It uses Resource API (high-level) of Boto3.

import os
import boto3
import botocore

# Instantiate the service resource object
s3_resource = boto3.resource('s3')

def lambda_handler(event, context):
    source_bucket_name = event['Records'][0]['s3']['bucket']['name']
    source_key = event['Records'][0]['s3']['object']['key']
    # Retrieve environment variable TARGET_BUCKET
    destination_bucket_name = os.environ.get('TARGET_BUCKET', None)
    if destination_bucket_name is None:
        # Environment variable TARGET_BUCKET does not exist
        print('Error: TARGET_BUCKET Lambda environment variable does not exist!!')
        return
    destination_key = source_key
    print('From - bucket: ' + source_bucket_name)
    print('From - object: ' + source_key)
    print('To   - bucket: ' + destination_bucket_name)
    print('To   - object: ' + destination_key)

    try:
        print('Moving object ...')
        #  Instantiate the destination bucket
        dest_bucket = s3_resource.Bucket(destination_bucket_name)
        # Copy the object
        copy_source = {
            'Bucket': source_bucket_name,
            'Key': source_key
        }
        dest_bucket.copy(copy_source, destination_key)
        #  Instantiate the source bucket
        source_bucket = s3_resource.Bucket(source_bucket_name)
        # Delete the object from source bucket
        source_obj = source_bucket.Object(source_key)
        response = source_obj.delete()
        print(response)
        print('\nMoved')

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "AccessDenied":
            print("Error: Access denied!!")
        elif e.response['Error']['Code'] == "InvalidBucketName":
            print("Error: Invalid bucket name!!")
        elif e.response['Error']['Code'] == "NoSuchBucket":
            print("Error: No such bucket!!")
        else:
            raise

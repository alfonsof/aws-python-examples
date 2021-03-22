# lamdda_function.py
# It handles an AWS Lambda function that copies an object when it appears
# in a S3 bucket to another S3 bucket.
# It uses Client API (low-level) of Boto3.

import os
import boto3
import botocore

# Create an S3 Client
s3_client = boto3.client('s3')

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

    # Copy the object
    try:
        print('Copying object ...')
        copy_source = {
            'Bucket': source_bucket_name,
            'Key': source_key
        }
        s3_client.copy(copy_source, destination_bucket_name, destination_key)
        print('Copied')

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "AccessDenied":
            print("Error: Access denied!!")
        elif e.response['Error']['Code'] == "InvalidBucketName":
            print("Error: Invalid bucket name!!")
        elif e.response['Error']['Code'] == "NoSuchBucket":
            print("Error: No such bucket!!")
        else:
            raise

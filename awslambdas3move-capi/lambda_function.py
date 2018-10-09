# lamdda_function.py
# It handles an AWS Lambda function that moves an object when it appears
# in a S3 bucket to another S3 bucket.
# It uses Client API (low-level) of Boto3.

import boto3
import botocore

# Create as S3 Client
s3client = boto3.client('s3')

def lambda_handler(event, context):
  DESTINATION_BUCKET = 'targetvm'      # Destination bucket name

  source_bucket_name = event['Records'][0]['s3']['bucket']['name']
  source_key = event['Records'][0]['s3']['object']['key']
  destination_bucket_name = DESTINATION_BUCKET
  destination_key = source_key
  print('From - bucket: ' + source_bucket_name)
  print('From - object: ' + source_key)
  print('To   - bucket: ' + destination_bucket_name)
  print('To   - object: ' + destination_key)

  try:
    # Copy the object
    print('Moving object ...')
    copy_source = {
      'Bucket': source_bucket_name,
      'Key': source_key
    }
    s3client.copy(copy_source, destination_bucket_name, destination_key)
    # Delete the object from source bucket
    response = s3client.delete_object(Bucket=source_bucket_name, Key=source_key)
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

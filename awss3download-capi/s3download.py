#!/usr/bin/python
# -*- coding: utf-8 -*-
# s3download.py
# s3download is an example that handles S3 buckets on AWS
# It uses Client API (low-level) of Boto3
# Download an object from a S3 bucket to a local file
# You must provide 1 parameter:
# BUCKET_NAME     = Name of the bucket
# OBJECT_NAME     = Object file name in the bucket
# LOCAL_FILE_NAME = Local file name

import sys
import boto3
import botocore

def main():

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if len(args) < 3:
    print('Not enough parameters. Proper Usage is: python s3download.py <BUCKET_NAME> <OBJECT_NAME> <LOCAL_FILE_NAME>')
    sys.exit(1)

  bucket_name = args[0]
  key_name = args[1]
  download_file_name = args[2]

  print('Bucket:     ' + bucket_name)
  print('Object/Key: ' + key_name)
  print('Local file: ' + download_file_name)

  # Create an S3 Client
  s3client = boto3.client('s3')

  # Download object
  try:
    print('Downloading object...')
    s3client.download_file(bucket_name, key_name, download_file_name)
    print('\nDownloaded')
  except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
      print("Error: Not Found, problem with the parameters!!")
    elif e.response['Error']['Code'] == "400":
      print("Error: Bad request, problem with the bucket!!")
    else:
      raise

  return


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

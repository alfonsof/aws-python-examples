# lamdda_function.py
# It handles an AWS Lambda function that sends information to the log about
# an object when it appears in a S3 bucket.

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key_name = event['Records'][0]['s3']['object']['key']

    print("Input:", event)
    print("Bucket:", bucket_name)
    print("Object:", key_name)

# lamdda_function.py
# It handles a simple AWS Lambda function that shows the content (text) of the call
# to the lambda function and returns a message including this content.

def lambda_handler(event, context):
    return 'Hello ' + event

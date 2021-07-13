# lamdda_function.py
# It handles an AWS Lambda function that it is invoked by an http request.
# It shows the parameters of the request and reponds a message including the parameters.

import json

def lambda_handler(event, context):
    if 'queryStringParameters' in event:    # If parameters
        print(event['queryStringParameters']['first_name'])
        print(event['queryStringParameters']['last_name'])
        body = 'Hello {} {}!'.format(event['queryStringParameters']['first_name'], 
                                    event['queryStringParameters']['last_name'])  
    else:    # If no parameters
        print('No parameters!')
        body = 'Who are you?'
        
    return {
        'statusCode': 200,
        'body': json.dumps(body)
    }

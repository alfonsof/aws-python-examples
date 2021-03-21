# lamdda_function.py
# It handles a simple AWS Lambda function that shows the content (JSON) of the call
# to the lambda function and returns a message including this content.

def lambda_handler(event, context):
    message = 'Hello {} {}!'.format(event['first_name'], 
                                    event['last_name'])  
    return { 
        'message' : message
    } 

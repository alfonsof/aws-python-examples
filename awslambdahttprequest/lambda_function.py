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

# https://oesnotu7ne.execute-api.eu-west-1.amazonaws.com/default/HttpRequestPython?first_name=Peter&last_name=Parker


{'version': '2.0', 'routeKey': 'GET /HttpRequestPython', 'rawPath': '/default/HttpRequestPython', 'rawQueryString': 'first_name=Peter&last_name=Parker', 'headers': {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3', 'cache-control': 'max-age=0', 'content-length': '0', 'host': 'oesnotu7ne.execute-api.eu-west-1.amazonaws.com', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0', 'x-amzn-trace-id': 'Root=1-60edae76-099272b12272fd32162fc1ee', 'x-forwarded-for': '87.125.176.151', 'x-forwarded-port': '443', 'x-forwarded-proto': 'https'}, 'queryStringParameters': {'first_name': 'Peter', 'last_name': 'Parker'}, 'requestContext': {'accountId': '617184998144', 'apiId': 'oesnotu7ne', 'domainName': 'oesnotu7ne.execute-api.eu-west-1.amazonaws.com', 'domainPrefix': 'oesnotu7ne', 'http': {'method': 'GET', 'path': '/default/HttpRequestPython', 'protocol': 'HTTP/1.1', 'sourceIp': '87.125.176.151', 'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}, 'requestId': 'CagyliOujoEEJmg=', 'routeKey': 'GET /HttpRequestPython', 'stage': 'default', 'time': '13/Jul/2021:15:17:10 +0000', 'timeEpoch': 1626189430751}, 'isBase64Encoded': False}

# AWS Lambda Function Http Request Python example

This folder contains an AWS Lambda Function example in Python on AWS (Amazon Web Services).

It handles an AWS Lambda function that it is invoked by an http request. It shows the parameters of the request and responds a message including the parameters.

## Requirements

* You must have an [Amazon Web Services (AWS)](http://aws.amazon.com/) account.

* The code was written for Python 3.

## Using the code

* Access the AWS console.

* Select AWS Lambda in the services menu.

* Create an AWS lambda function.
  * Name: `<LAMBDA_NAME>`
  * Runtime: `Python 3.8`
  * Handler: `lambda_function.lambda_handler`
  * Role: `lambda-basic-execution`
  * Runtime Settings for the lambda function:
    * Memory (MB): `128`
    * Timeout: `3 sec`
  * The resources that the function's role has access to:
    * `Amazon CloudWatch Logs`
  * The triggers:
    * `API Gateway`
      * Details below.

* Write the code of the Lambda funtion.

  The content of `lambda_function.py` file.

* Deploy the Lambda function.

  It deploys the Lambda function to AWS.

* Create an `API Gateway` trigger.

  This allows to call the lambda function using an HTTP API.

  * Name: `<LAMBDA_NAME>-API`
  * API: `Create an API`
  * API type: `HTTP API`
  * Security: `Open`

  You will get an API endpoint, which can be copied and run in your browser's address bar.
  
  It looks like the following URL:
  
  ```bash
  https://<API_ID>.execute-api.<REGION>.amazonaws.com/<STAGE_NAME>/<LAMBDA_NAME>
  ```

  For example:

  ```bash
  https://abcdefg5jk.execute-api.eu-west-1.amazonaws.com/default/HttpRequestPython`
  ```

* Run the code.

  To run the code, you need to use 2 parameters:

  * `first_name`
  * `last_name`

  You call the API endpoint with this format: 
  
  ```bash
  https://<API_ID>.execute-api.<REGION>.amazonaws.com/<STAGE_NAME>/<LAMBDA_NAME>?first_name=<FIRST_NAME>&last_name=<LAST_NAME>
  ```

  For example:

  ```bash
  https://abcdefg5jk.execute-api.eu-west-1.amazonaws.com/default/HttpRequestPython?first_name=Peter&last_name=Parker
  ```

* Test the AWS Lambda function.

  Go to the URL of API endpoint that you have got: `https://<API_ID>.execute-api.<REGION>.amazonaws.com/<STAGE_NAME>/<LAMBDA_NAME>?first_name=Peter&last_name=Parker` using a browser.

  You should see the next response if you have added the right paramenters:

  ```bash
  "Hello Peter Parker!"
  ```

  You should see the next response if you have not added any paramenter:

  ```bash
  "Who are you?"
  ```
  
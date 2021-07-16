# Python examples on AWS (Amazon Web Services)

This repo contains Python code examples on AWS (Amazon Web Services).

These examples show how to use Python 3 and Boto 3 in order to manage Amazon services on AWS. These use Resource API (high-level) and Client API (low-level) of Boto 3.

Boto 3 is the AWS (Amazon Web Services) SDK for Python, which allows Python developers to write software that makes use of Amazon services like EC2 and S3. Boto provides an easy to use, object-oriented API as well as low-level direct service access.

Boto 3 offers two different styles of API:

* Resource API (high-level): It provides an object-oriented abstraction on top (object.delete(), object.put(), etc.).
* Client API (low-level): It maps directly to the underlying RPC-style service operations (put_object, delete_object, etc.).

## Quick start

You must have an [AWS (Amazon Web Services)](http://aws.amazon.com/) account.

The code for the samples is contained in individual folders on this repository.

For instructions on running the code, please consult the README in each folder.

This is the list of examples:

**Compute - Amazon EC2:**

* Using the Client API (low-level) of Boto 3:
  * [awsec2instances-capi](/awsec2instances-capi) - AWS EC2 instances (Client API): Example of how to handle AWS EC2 instances. It uses the Client API (low-level) of Boto 3.

* Using the Resource API (high-level) of Boto 3:
  * [awsec2instances-rapi](/awsec2instances-rapi) - AWS EC2 instances (Resource API): Example of how to handle AWS EC2 instances. It uses the Resource API (high-level) of Boto 3.

**Compute - AWS Lambda:**

* Lambda function handler:
  * [awslambdahello](/awslambdahello) - AWS Lambda Function Hello World: Example of how to handle an AWS simple Lambda function and a text input.
  * [awslambdahellojson](/awslambdahellojson) - AWS Lambda Function Hello World JSON: Example of how to handle an AWS simple Lambda  function and a JSON input.
  * [awslambdahttprequest](/awslambdahttprequest) - AWS Lambda Function Http Request: Example of how to handle an AWS Lambda Function, show the parameters of the request and repond a message including the parameters.
  * [awslambdas3event](/awslambdas3event) - AWS Lambda Function S3 Event: Example of how to handle an AWS Lambda Function and send information to the log about an object when it appears in a S3 bucket.

* Lambda function handler using the Client API (low-level) of Boto 3:
  * [awslambdas3copy-capi](/awslambdas3copy-capi) - AWS Lambda Function S3 Copy: Example of how to handle an AWS Lambda function and copy an object when it appears in a S3 bucket to another S3 bucket. It uses the Client API (low-level) of Boto 3.
  * [awslambdas3move-capi](/awslambdas3move-capi) - AWS Lambda Function S3 Move: Example of how to handle an AWS Lambda function and move an object when it appears in a S3 bucket to another S3 bucket. It uses the Client API (low-level) of Boto 3.
  
* Lambda function handler using the Resource API (high-level) of Boto 3:
  * [awslambdas3copy-rapi](/awslambdas3copy-rapi) - AWS Lambda Function S3 Copy: Example of how to handle an AWS Lambda function and copy an object when it appears in a S3 bucket to another S3 bucket. It uses the Resource API (high-level) of Boto 3.
  * [awslambdas3move-rapi](/awslambdas3move-rapi) - AWS Lambda Function S3 Move: Example of how to handle an AWS Lambda function and move an object when it appears in a S3 bucket to another S3 bucket. It uses the Resource API (high-level) of Boto 3.

* Lambda service client - Service operations - Using the Client API (low-level) of Boto 3:
  * [awslambdacreate-capi](/awslambdacreate-capi) - AWS Lambda Function Create: Example of how to handle an AWS Lambda function and create it. It uses the Client API (low-level) of Boto 3.
  * [awslambdaupdate-capi](/awslambdaupdate-capi) - AWS Lambda Function Update: Example of how to handle an AWS Lambda function and update it. It uses the Client API (low-level) of Boto 3.
  * [awslambdainvoke-capi](/awslambdainvoke-capi) - AWS Lambda Function Invoke: Example of how to handle an AWS Lambda function and invoke it. It uses the Client API (low-level) of Boto 3.
  * [awslambdalist-capi](/awslambdalist-capi) - AWS Lambda Function List: Example of how to handle an AWS Lambda function and list its information. It uses the Client API (low-level) of Boto 3.
  * [awslambdalistall-capi](/awslambdalistall-capi) - AWS Lambda Function List All: Example of how to handle AWS Lambda functions and list all Lambda functions and their information. It uses the Client API (low-level) of Boto 3.
  * [awslambdadelete-capi](/awslambdadelete-capi) - AWS Lambda Function Delete: Example of how to handle an AWS Lambda function and delete it. It uses the Client API (low-level) of Boto 3.

**Storage - Amazon S3:**

* Using the Client API (low-level) of Boto 3:
  * [awss3create-capi](/awss3create-capi) - AWS S3 Create (Client API): Example of how to handle S3 buckets and create a new S3 bucket. It uses the Client API (low-level) of Boto 3.
  * [awss3delete-capi](/awss3delete-capi) - AWS S3 Delete (Client API): Example of how to handle S3 buckets and delete a S3 bucket. It uses the Client API (low-level) of Boto 3.
  * [awss3list-capi](/awss3list-capi) - AWS S3 List (Client API): Example of how to handle S3 buckets and list information about objects in a S3 bucket. It uses the Client API (low-level) of Boto 3.
  * [awss3listall-capi](/awss3listall-capi) - AWS S3 List All (Client API): Example of how to handle S3 buckets and list information about all S3 buckets and the objects they contain. It uses the Client API (low-level) of Boto 3.
  * [awss3upload-capi](/awss3upload-capi) - AWS S3 List (Client API): Example of how to handle S3 buckets and upload a local file to a S3 bucket. It uses the Client API (low-level) of Boto 3.
  * [awss3download-capi](/awss3download-capi) - AWS S3 List (Client API): Example of how to handle S3 buckets and download an object from a S3 bucket to a local file. It uses the Client API (low-level) of Boto 3.
  * [awss3deleteobject-capi](/awss3deleteobject-capi) - AWS S3 Delete Object (Client API): Example of how to handle S3 buckets and delete an object in a S3 bucket. It uses the Client API (low-level) of Boto 3.
  * [awss3copy-capi](/awss3copy-capi) - AWS S3 Copy (Client API): Example of how to handle S3 buckets and copy an object from a S3 bucket to another S3 bucket. It uses the Client API (low-level) of Boto 3.
  * [awss3move-capi](/awss3move-capi) - AWS S3 Move (Client API): Example of how to handle S3 buckets and move an object from a S3 bucket to another S3 bucket. It uses the Client API (low-level) of Boto 3.

* Using the Resource API (high-level) of Boto 3:
  * [awss3create-rapi](/awss3create-rapi) - AWS S3 Create (Resource API): Example of how to handle S3 buckets and create a new S3 bucket. It uses the Resource API (high-level) of Boto 3.
  * [awss3delete-rapi](/awss3delete-rapi) - AWS S3 Delete (Resource API): Example of how to handle S3 buckets and delete a S3 bucket. It uses the Resource API (high-level) of Boto 3.
  * [awss3list-rapi](/awss3list-rapi) - AWS S3 List (Resource API): Example of how to handle S3 buckets and list information about objects in a S3 bucket. It uses the Resource API (high-level) of Boto 3.
  * [awss3listall-rapi](/awss3listall-rapi) - AWS S3 List All (Resource API): Example of how to handle S3 buckets and list information about all S3 buckets and the objects they contain. It uses the Resource API (high-level) of Boto 3.
  * [awss3upload-rapi](/awss3upload-rapi) - AWS S3 List (Resource API): Example of how to handle S3 buckets and upload a local file to a S3 bucket. It uses the Resource API (high-level) of Boto 3.
  * [awss3download-rapi](/awss3download-rapi) - AWS S3 List (Resource API): Example of how to handle S3 buckets and download an object from a S3 bucket to a local file. It uses the Resource API (high-level) of Boto 3.
  * [awss3deleteobject-rapi](/awss3deleteobject-rapi) - AWS S3 Delete Object (Resource API): Example of how to handle S3 buckets and delete an object in a S3 bucket. It uses the Resource API (high-level) of Boto 3.
  * [awss3copy-rapi](/awss3copy-rapi) - AWS S3 Copy (Resource API): Example of how to handle S3 buckets and copy an object from a S3 bucket to another S3 bucket. It uses the Resource API (high-level) of Boto 3.
  * [awss3move-rapi](/awss3move-rapi) - AWS S3 Move (Resource API): Example of how to handle S3 buckets and move an object from a S3 bucket to another S3 bucket. It uses the Resource API (high-level) of Boto 3.
  
## License

This code is released under the MIT License. See LICENSE file.

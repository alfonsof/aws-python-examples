# Python examples on AWS (Amazon Web Services)

This repo contains Python code examples on AWS (Amazon Web Services).

These examples show how to use Python 3 and Boto 3 in order to manage Amazon services on AWS. These use Resource API (high-level) and Client API (low-level) of Boto 3.

Boto is the AWS (Amazon Web Services) SDK for Python, which allows Python developers to write software that makes use of Amazon services like S3 and EC2. Boto provides an easy to use, object-oriented API as well as low-level direct service access.

Boto 3 offers two different styles of API:

* Resource API (high-level): It provides an object-oriented abstraction on top (object.delete(), object.put(), etc.).
* Client API (low-level): It maps directly to the underlying RPC-style service operations (put_object, delete_object, etc.).

## Quick start

You must have an [AWS (Amazon Web Services)](http://aws.amazon.com/) account.

The code for the samples is contained in individual folders on this repository. You can see the list:

**Storage - Amazon S3:**

* Using the Boto3 Client API (low-level)
  * [awss3create-capi](/awss3create-capi) - AWS S3 Create (Client API): Example of how to handle S3 buckets and create a new S3 bucket using the Client API (low-level).
  * [awss3delete-capi](/awss3delete-capi) - AWS S3 Delete (Client API): Example of how to handle S3 buckets and delete a  S3 bucket using the Client API (low-level).
  * [awss3listall-capi](/awss3listall-capi) - AWS S3 List All (Client API): Example of how to handle S3 buckets and list information about all S3 buckets and the objects they contain using the Client API (low-level).
  * [awss3list-capi](/awss3list-capi) - AWS S3 List (Client API): Example of how to handle S3 buckets and list information about objects in a S3 bucket using the Client API (low-level).
  * [awss3copy-capi](/awss3copy-capi) - AWS S3 Copy (Client API): Example of how to handle S3 buckets and copy an object from a S3 bucket to another S3 bucket using the Client API (low-level).
  * [awss3move-capi](/awss3move-capi) - AWS S3 Move (Client API): Example of how to handle S3 buckets and move an object from a S3 bucket to another S3 bucket using the Client API (low-level).
  * [awss3upload-capi](/awss3upload-capi) - AWS S3 List (Client API): Example of how to handle S3 buckets and upload a local file to a S3 bucket using the Client API (low-level).
  * [awss3download-capi](/awss3download-capi) - AWS S3 List (Client API): Example of how to handle S3 buckets and download an object from a S3 bucket to a local file using the Client API (low-level).

* Using the Boto3 Resource API (high-level)
  * [awss3create-rapi](/awss3create-rapi) - AWS S3 Create (Resource API): Example of how to handle S3 buckets and create a new S3 bucket using the Resource API (high-level).
  * [awss3delete-rapi](/awss3delete-rapi) - AWS S3 Delete (Resource API): Example of how to handle S3 buckets and delete a S3 bucket using the Resource API (high-level).
  * [awss3listall-rapi](/awss3listall-rapi) - AWS S3 List All (Resource API): Example of how to handle S3 buckets and list information about all S3 buckets and the objects they contain using the Resource API (high-level).
  * [awss3list-rapi](/awss3list-rapi) - AWS S3 List (Resource API): Example of how to handle S3 buckets and list information about objects in a S3 bucket using the Resource API (high-level).
  * [awss3copy-rapi](/awss3copy-rapi) - AWS S3 Copy (Resource API): Example of how to handle S3 buckets and copy an object from a S3 bucket to another S3 bucket using the Resource API (high-level).
  * [awss3move-rapi](/awss3move-rapi) - AWS S3 Move (Resource API): Example of how to handle S3 buckets and move an object from a S3 bucket to another S3 bucket using the Resource API (high-level).
  * [awss3upload-rapi](/awss3upload-rapi) - AWS S3 List (Resource API): Example of how to handle S3 buckets and upload a local file to a S3 bucket using the Resource API (high-level).
  * [awss3download-rapi](/awss3download-rapi) - AWS S3 List (Resource API): Example of how to handle S3 buckets and download an object from a S3 bucket to a local file using the Resource API (high-level).

For instructions on running the code, please consult the README in each folder.

## License

This code is released under the MIT License. See LICENSE file.

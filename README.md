# Python examples on AWS (Amazon Web Services)

This repo contains Python code examples on AWS (Amazon Web Services).

## Quick start

You must have an [AWS (Amazon Web Services)](http://aws.amazon.com/) account.

The code for the samples is contained in individual folders on this repository. You can see the list:

**Storage - Amazon S3:**

* Using the Boto3 Client API (low-level)
  * [awss3create-capi](/awss3create-capi) - AWS S3 Create (Client API): Example of how to handle S3 buckets and create a new S3 bucket using the Client API (low-level).
  * [awss3delete-capi](/awss3delete-capi) - AWS S3 Delete (Client API): Example of how to handle S3 buckets and delete a  S3 bucket using the Client API (low-level).
  * [awss3listall-capi](/awss3listall-capi) - AWS S3 List All (Client API): Example of how to handle S3 buckets and  list information about all S3 buckets and the files they contain.

* Using the Boto3 Resource API (high-level)
  * [awss3create-rapi](/awss3create-rapi) - AWS S3 Create (Resource API): Example of how to handle S3 buckets and create a new S3 bucket using the Resource API (high-level).
  * [awss3delete-rapi](/awss3delete-rapi) - AWS S3 Delete (Resource API): Example of how to handle S3 buckets and delete a S3 bucket using the Resource API (high-level).
  * [awss3listall-rapi](/awss3listall-rapi) - AWS S3 List All (Resource API): Example of how to handle S3 buckets and  list information about all S3 buckets and the files they contain.

For instructions on running the code, please consult the README in each folder.

## License

This code is released under the MIT License. See LICENSE file.
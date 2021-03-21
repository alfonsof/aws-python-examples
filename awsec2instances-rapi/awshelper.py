#!/usr/bin/python
# -*- coding: utf-8 -*-
# awshelper.py
# It has methods for managing AWS EC2 instances.
# It uses Resource API (high-level) of Boto3.

import sys
import boto3
import botocore

region = 'eu-west-1'    # AWS region

def describe_instances():
    """
    Describes all EC2 instances associated with an AWS account
    """
    # Instantiate the service resource object
    ec2_resource = boto3.resource('ec2', region_name=region)
    # Describe instances
    instances = ec2_resource.instances.all()
    for instance in instances:
        print('State of the instance "' + instance.id + '" is: "' + instance.state['Name'] + '"')
    return


def run_instance():
    """
    Run an EC2 instance
    """
    ami_id        = "ami-785db401"   # AMI Id
    instance_type = "t2.micro"       # Instance Type

    # Instantiate the service resource object
    ec2_resource = boto3.resource('ec2', region_name=region)
    # Run an instance
    instances = ec2_resource.create_instances(ImageId=ami_id, InstanceType=instance_type,
                                              MaxCount=1, MinCount=1)
    Instance_id = instances[0].id
    print('\nInstance Id:      ' + Instance_id)
    print('Image Id:         ' + instances[0].image_id)
    print('Instance Type:    ' + instances[0].instance_type)
    print('State:            ' + instances[0].state['Name'])
    return Instance_id


def describe_instance(instance_id):
    """
    Describes an EC2 instance
    """
    # Instantiate the service resource object
    ec2_resource = boto3.resource('ec2', region_name=region)
    try:
        # Describe an instance
        instance = ec2_resource.Instance(instance_id)
        print('\nInstance Id:      ' + instance_id)
        print('Instance Id:      ' + instance.id)
        print('Image Id:         ' + instance.image_id)
        print('Instance Type:    ' + instance.instance_type)
        print('State:            ' + instance.state['Name'])
        if instance.state['Name'] == 'running':
            print('Private DNS Name: ' + instance.private_dns_name)
            print('Private IP:       ' + instance.private_ip_address)
            print('Public DNS Name:  ' + instance.public_dns_name)
            print('Public IP:        ' + instance.public_ip_address)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "MissingParameter":
            print("Error: Missing instance id!!")
        else:
            raise
    return


def start_instance(instance_id):
    """
    Start an EC2 instance
    """
    # Instantiate the service resource object
    ec2_resource = boto3.resource('ec2', region_name=region)
    try:
        # Start an instance
        response = ec2_resource.Instance(instance_id).start(DryRun=False)
        print(response)
        print("\nSuccessfully starting instance: ", instance_id)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "InvalidInstanceID.Malformed":
            print("Error: Invalid instance id!!")
        else:
            raise
    return


def stop_instance(instance_id):
    """
    Stop an EC2 instance
    """
    # Instantiate the service resource object
    ec2_resource = boto3.resource('ec2', region_name=region)
    try:
        # Stop an instance
        response = ec2_resource.Instance(instance_id).stop(DryRun=False)
        print(response)
        print("\nSuccessfully stopping instance: ", instance_id)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "InvalidInstanceID.Malformed":
            print("Error: Invalid instance id!!")
        else:
            raise
    return


def reboot_instance(instance_id):
    """
    Reboot an EC2 instance
    """
    # Instantiate the service resource object
    ec2_resource = boto3.resource('ec2', region_name=region)
    try:
        # Reboot an instance
        response = ec2_resource.Instance(instance_id).reboot(DryRun=False)
        print(response)
        print("\nSuccessfully rebooting instance: ", instance_id)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "InvalidInstanceID.Malformed":
            print("Error: Invalid instance id!!")
        else:
            raise
    return


def terminate_instance(instance_id):
    """
    Terminate an EC2 instance
    """
    # Instantiate the service resource object
    ec2_resource = boto3.resource('ec2', region_name=region)
    try:
        # Terminate an instance
        response = ec2_resource.Instance(instance_id).terminate(DryRun=False)
        print(response)
        print("\nSuccessfully terminating instance: ", instance_id)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "InvalidInstanceID.Malformed":
            print("Error: Invalid instance id!!")
        else:
            raise
    return

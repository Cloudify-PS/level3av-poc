#!/usr/bin/env python

from cloudify import ctx
from cloudify.state import ctx_parameters as inputs
# import subprocess
# import sys

# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'boto3'])
import boto3


ec2_client = boto3.client('ec2',
                          aws_access_key_id=inputs['aws_access_key_id'],
                          aws_secret_access_key=inputs['aws_secret_access_key'],
                          region_name=inputs['region'])

security_groups = ec2_client.describe_security_groups(
    Filters=[{
        'Name': 'vpc-id',
        'Values': [inputs['vpc_id']]
    }]
)

for security_group in security_groups['SecurityGroups']:
    if security_group['GroupName'] == 'default':
        ctx.instance.runtime_properties['default_sg_id'] = \
            security_group['GroupId']
        ec2_client.create_tags(
            Resources=[security_group['GroupId']],
            Tags=[{'Key':'Name', 'Value':inputs['sg_name']}]
        )
        break

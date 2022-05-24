#!/usr/bin/env python

import boto3
from cloudify import ctx
from cloudify.state import ctx_parameters as inputs


ec2_client = boto3.client('ec2',
                          aws_access_key_id=inputs['aws_access_key_id'],
                          aws_secret_access_key=inputs['aws_secret_access_key'],
                          region_name=inputs['region'])



route_table = ec2_client.describe_route_tables(
    Filters=[{
        'Name': 'route-table-id',
        'Values': [inputs['route_table_id']]
    }]
).get('RouteTables')[0]

ctx.logger.debug('route_table: {}'.format(route_table))

associations = [
    obj['RouteTableAssociationId'] for obj in route_table['Associations']
]
ctx.logger.debug('Associations: {}'.format(associations))

for association_id in associations:
    ec2_client.disassociate_route_table(AssociationId=association_id)

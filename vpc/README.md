# VPC

This blueprint uses the [Cloudify AWS Plugin](https://docs.cloudify.co/latest/working_with/official_plugins/infrastructure/aws/) to deploy a VPC with the following resources:

* VPC
* Two public subnets (primary and secondary)
* Two private subnets (primary and secondary)
* Gateway management security group and rules
* Gateway data security group and rules

Resources are tagged with the name of the customer, which is provided as an input.

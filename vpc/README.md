# VPC

This blueprint uses the [Cloudify AWS Plugin](https://docs.cloudify.co/latest/working_with/official_plugins/infrastructure/aws/) to deploy a VPC with the following resources:

* Two public subnets (primary and secondary)
* Two private subnets (primary and secondary)
* Gateway management security group and rules
* Gateway data security group and rules

Also, the [new_vpc.yaml](../new_vpc.yaml) creates a new VPC as a base for all above-mentioned resources.  
The [existing_vpc.yaml](../existing_vpc.yaml) uses a VPC which already exists.  
Resources are tagged with the name of the customer, which is provided as an input.  

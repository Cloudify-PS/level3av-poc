# Crestron-VC-4

This blueprint uses the [Cloudify AWS Plugin](https://docs.cloudify.co/latest/working_with/official_plugins/infrastructure/aws/) to deploy cloud resources, such as:

* Keypair
* Security Group with rules
* NIC
* EC2 instance for Crestron-VC-4
* CloudInit config to initially configure the EC2 instance

It also uses the [Cloudify Ansible Plugin](https://docs.cloudify.co/latest/working_with/official_plugins/orchestration/ansible/) to run the _installvc4_ Ansible Playbook on the newly created virtual machine.

Blueprint exposes the following capabilities:
* ami_id - the ID of AMI used for EC2 instance
* server_ip - the public IP address of the EC2 instance

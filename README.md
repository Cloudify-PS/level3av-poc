# level3av-poc

A deployment of Zabbix monitoring instance ([blueprint](zabbix.yaml), [ReadMe](zabbix-helm/README.md)) on top of EKS cluster ([blueprint](eks.yaml), [ReadMe](eks/README.md)) and RDS database ([blueprint](rds.yaml), [ReadMe](rds/README.md)) with all necessary networking resources ([blueprint](vpc.yaml), [ReadMe](vpc/README.md)).  

To create the infrastructure:
- make sure you have the following [plugins](https://cloudify.co/plugins/) installed on your Cloudify Manager instance:
    - [Cloudify AWS Plugin](https://github.com/cloudify-cosmo/cloudify-aws-plugin/releases)
    - [Cloudify Kubernetes Plugin](https://github.com/cloudify-cosmo/cloudify-kubernetes-plugin/releases)
    - [Cloudify Helm Plugin](https://github.com/cloudify-incubator/cloudify-helm-plugin/releases)
    - [Cloudify Utilities Plugin](https://github.com/cloudify-incubator/cloudify-utilities-plugin/releases)
- make sure you have all the necessary secrets created and set up:
    - aws_access_key_id
    - aws_secret_access_key
- upload the [blueprint](blueprint.yaml) to your Cloudify Manager, most preferably using the URL: https://github.com/Cloudify-PS/level3av-poc/archive/refs/heads/main.zip  
  (for the existing VPC and network option, choose [blueprint_existing_network.yaml](blueprint_existing_network.yaml))
- create and install a deployment providing your desired configuration in inputs

The main deployment exposes the following outputs:
- _rds_endpoint_ - RDS endpoint address
- _eks_endpoint_ - EKS endpoint address
- _zabbix_endpoint_ - the HTTP endpoint for accessing the Zabbix web interface

## Crestron VC-4
A deployment of Crestron VC-4 instance configured using provided Ansible Playbook.  
More details in the [ReadMe](crestron-vc4/README.md).  

## Trustgrid
A deployment of Trustgrid infrastructure declared in the Terraform files.  
More details in the [ReadMe](trustgrid/README.md).  

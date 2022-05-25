# EKS

This blueprint uses the [Cloudify AWS Plugin](https://docs.cloudify.co/latest/working_with/official_plugins/infrastructure/aws/) to deploy an EKS cluster.  

Blueprint creates the following resources:
* Keypair
* IAM Role for EKS Service
* IAM Role for EKS Node Group
* EKS Cluster
* EKS Node Group
* Kubernetes Service Account

Blueprint exposes the following capabilities:
* endpoint - the endpoint of the EKS Cluster
* connection_details - details of the connection to the cluster, kubeconf file

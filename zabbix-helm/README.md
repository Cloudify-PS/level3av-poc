# Zabbix

This blueprint uses the [Cloudify Kubernetes Plugin](https://docs.cloudify.co/latest/working_with/official_plugins/orchestration/kubernetes/) and the [Cloudify Helm Plugin](https://docs.cloudify.co/latest/working_with/official_plugins/orchestration/helm/) to deploy a Zabbix service with the following resources:

* Helm binary installation
* Zabbix repository (https://cetic.github.io/helm-charts)
* Zabbix release
* Zabbix Kubernetes Service

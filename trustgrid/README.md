# Trustgrid

This blueprints use the [Cloudify Terraform Plugin](https://docs.cloudify.co/latest/working_with/official_plugins/orchestration/terraform/) to deploy the infrastructure declared in the provided terraform files.  

There are 3 separate versions of the blueprint:
* trustgrid_local_tf.yaml - takes the terraform files locally from the Blueprint zip file.
* trustgrid_remote_tf.yaml - takes the terraform files from the remote zip file by the URL provided in input.
* trustgrid_remote_release_tf.yaml - takes the terraform files from the GitHub repository. The URL of GitHub repository and Release/Tag are provided in inputs.

By default, the Terraform backend is set to be local. To use remote backend, you need to uncomment the _terraform_login_token_ node in the desired blueprint and provide the token in a secret called _terraform_token_.  

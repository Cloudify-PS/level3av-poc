#!/usr/bin/env bash


mkdir -p ~/.terraform.d
cat << EOL > ~/.terraform.d/credentials.tfrc.json
{
  "credentials": {
    "app.terraform.io": {
      "token": "${terraform_token}"
    }
  }
}
EOL

This repo streamlines the deployment of new VC-4 instances as well patching, certificate management, and user lifecycle tasks. 
The ./fullinstallVC-4.yml playbook is idempotent and awesome. 

Features:
- Automated deployment from scratch AlmaLinux 8.2+ server. Includes downloading of VC-4 packages and complete installation and configuration.
- Fully idempotent. Can run against the same host over and over non-destructively. 
- Automates patching of VC-4 servers. The script will fetch he latest security patches and dependencies unless otherwise pinned. 
- Observable. Provides visibility into the SBOM of VC-4 and all configuration steps. 
- HTTPS only (self-signed) out of the box. All HTTP requests redirect to HTTPS. 
- Authentication out of the box. Separate PAM user groups for read-only and read-write permissions (webusers & webadmins respectively) for logon to the VC-4 web page
- Surfaces the device_resolution.cfg file via the browser for read access: https://{SERVER_ADDRESS}/VirtualControl/conf/docs/device_resolution.cfg

TODO: 
- Randomly generate and store the mariadb root user passwords
- Deeper hardening of Linux
- Deeper hardening of Apache
- Loop through user accounts and create all across target hosts as needed (only needed if we need to add more accounts beyond webuser and webadmin)
- Work through LDAP / SAML2.0 PAM integration to move away from static accounts entirely
- Enable SSL certificate update based on a cert file being placed in this directory
- Add device_resolution.cfg to the playbook and project directory for easy & idempotent setting of resolution tables
- Enable setting a VC-4 version number as an argument at runtime or in an args file
- Enable VC-4 upgrades via DNF

Quickstart:
1. Prepare the guest. You'll need an AlmaLinux 8.2+ machine which has an appropriate public key enabled on it allowing SSH access. No other prep is needed on the guest. 
2. Add the guest to your inventory file (hosts.ini)
3. Run the fullInstallVC4.yml playbook with the primary options populated (sample below)
    - crestron_user=< a valid Crestron FTP site access username >
    - crestron_password= < a valid Crestron FTP site access password >
    - script_path=< the directory to download the scripts & rpm files to, default is /home/vc4admin >
    - install_path=< the directory to install VC-4 into, default /opt/crestron >
    - mariadb_password=< the MariaDB root user password to set >
4. Wait and be patient...the installer takes some time on the [Install / upgrade VC-4] task...around 5-10 minutes
5. When the playbook completes, put the IP address (or fqdn if already set) into your web browser and log in to VC-4!

Sample command: 
```

$ ansible-playbook ./installVC-4.yml -kK \
    -i hosts.ini \
    -e "crestron_user=<SOMEUSERACCOUNT> \
    crestron_password=<SOMEPASSWORD> \
    script_path=/home/vc4admin/ \
    install_path=/opt/crestron/ \
    mariadb_password=<SOMEOTHERPASSWORD>"

```

Sample inventory hosts.ini:
```

[vc-4-servers]
dev-vc4-vm1.bun.lab ansible_host=192.168.3.97
dev-vc4-vultr1 ansible_host=104.207.159.251

[vc-4-servers:vars]
ansible_user="vc4admin"
ansible_ssh_private_key_file=~/.ssh/vc4-ssh-key-A

```
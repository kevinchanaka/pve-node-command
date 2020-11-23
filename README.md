## Overview ##

Simple container that sends a reboot or shutdown command to a desired node in a proxmox environment. This will cause all VMs on the underlying node to shutdown gracefully before the node is shutdown or rebooted. 

For this script to function, all of the below environment variables must be passed to the container

| Environment Variable  | Description  |
|---|---|
| API_HOST  | Domain name/IP address of Proxmox API  |
| NODE_NAME  | Name of Proxmox node to shutdown  |
| TOKEN_USER |  Name of user assigned to Proxmox API token |
| TOKEN_NAME | Name of API token  |
| TOKEN_VALUE | Token value used to authenticate to Proxmox API  |
| COMMAND | Command to send to Proxmox node. Must either be 'shutdown' or 'reboot'. This value is set to 'shutdown' by default. |

## Setting Up ##

This container requires an API key that has the "Sys.PowerMgmt" privilige. For Proxmox version 6.2, the following steps can be performed to create an API token with this privilige
1. Navigate to "Datacenter" -> "Permissions" -> "API Tokens" and create a new token. Ensure that privilige separation is selected
2. Navigate to "Datacenter" -> "Permissions" -> "Roles" and create a new role with the "Sys.PowerMgmt" privilige
3. Naviage to "Datacenter" -> "Permissions" and create a new API token permission. Select "/nodes" as the path and select the API token and role created earlier. Ensure that the propagate flag is set.

For more information, please refer to the [Proxmox API docs](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/status) and the [Proxmox wiki](https://pve.proxmox.com/wiki/Proxmox_VE_API)

## Usage ##

Run the container with the following command:

```docker run --rm -d --env-file <PATH_TO_ENV_FILE> kevinchanaka/pve-node-shutdown```

The environment variable file would consist of the values of the environment variables, refer below for a sample
```
API_HOST=192.168.0.110
NODE_NAME=pve
TOKEN_USER=myuser
TOKEN_NAME=mytoken
TOKEN_VALUE=foobar
```

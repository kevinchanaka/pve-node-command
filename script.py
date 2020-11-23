import os 
import sys
from proxmoxer import ProxmoxAPI

env_vars = ["API_HOST", "NODE_NAME", "TOKEN_USER", "TOKEN_NAME", "TOKEN_VALUE", "COMMAND"]
env = {}
for var in env_vars:
    if os.environ[var] == "":
        print("Variable {} is not defined, please specify it as an environment variable or secret".format(var))
        sys.exit(1)
    if var == "COMMAND" and (os.environ[var] != "shutdown" and os.environ[var] != "reboot"):
        print("Variable COMMAND must either be 'shutdown' or 'reboot', not {}".format(COMMAND))
        sys.exit(1)
    env[var] = os.environ[var]

proxmox = ProxmoxAPI(env["API_HOST"], user=env["TOKEN_USER"], token_name=env["TOKEN_NAME"], token_value=env["TOKEN_VALUE"], verify_ssl=False)

try:
    node = [x for x in proxmox.nodes.get() if x["node"] == env["NODE_NAME"]]
except Exception as e:
    print("Authentication error, please check values provided for TOKEN_USER, TOKEN_NAME and TOKEN_VALUE")
    print(e)
    sys.exit(1)

if len(node) == 0:
    print("Node '{}' was not found in datacenter on '{}'".format(env["NODE_NAME"], env["API_HOST"]))
    sys.exit(1)
else:
    node = node[0]["node"]

print("Sending '{}' command to node '{}' at {}".format(env["COMMAND"], node, env["API_HOST"]))

try:
    proxmox.nodes.post("{}/status?command={}".format(node, env["COMMAND"]))
except Exception as e:
    print("Authorisation error, ensure that API key has sufficient permissions")
    print(e)
    sys.exit(1)

print("Command '{}' sent to node '{}'".format(env["COMMAND"], node))


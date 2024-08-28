import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ncclient import manager
from device_info import nexus_1

nxv = manager.connect(
    host=nexus_1['address'], 
    port=nexus_1['netconf_port'], 
    username=nexus_1['username'], 
    password=nexus_1['password'], 
    device_params={'name':'nexus'}, hostkey_verify=False)

for capability in nxv.server_capabilities:
    print(capability)
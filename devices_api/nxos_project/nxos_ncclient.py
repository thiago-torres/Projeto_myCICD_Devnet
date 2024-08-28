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

get_filter = "<filter><System xmlns='http://cisco.com/ns/yang/cisco-nx-os-device'></System></filter>"

get_config = nxv.get_config(source='running', filter=get_filter)#.data_xml
print(type(get_config))

print(get_config)
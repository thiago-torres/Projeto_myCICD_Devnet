import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ncclient import manager
from device_info import ios_xe_sandbox

if __name__ == '__main__':
    try:
        with manager.connect(
            host=ios_xe_sandbox['address'],
            port=ios_xe_sandbox['netconf_port'],
            username=ios_xe_sandbox['username'],
            password=ios_xe_sandbox['password'],
            hostkey_verify=False
        ) as m:           
            
            print("Here are the NETCONF Capabilities")
            for capability in m.server_capabilities:
                print(capability)

    except Exception as e:
        print(f"Erro de conexão: {e}")
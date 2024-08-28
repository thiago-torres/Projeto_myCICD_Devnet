import os
from ncclient import manager

if __name__ == '__main__':
    try:
        with manager.connect(
            host=os.getenv("IOS_XE_ADDRESS"),
            port=830,
            username=os.getenv("IOS_XE_USERNAME"),
            password=os.getenv("IOS_XE_PASSWORD"),
            hostkey_verify=False
        ) as m:           
            
            print("Here are the NETCONF Capabilities")
            for capability in m.server_capabilities:
                print(capability)

    except Exception as e:
        print(f"Erro de conexão: {e}")
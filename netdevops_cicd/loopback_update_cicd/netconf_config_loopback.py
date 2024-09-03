import os
from ncclient import manager

def main():
    try:
        with manager.connect(
            host=os.getenv("IOS_XE_ADDRESS"),
            port=830,
            username=os.getenv("IOS_XE_USERNAME"),
            password=os.getenv("IOS_XE_PASSWORD"),
            hostkey_verify=False
        ) as m:
            print("Conexão bem-sucedida")
            print('--------------------(1)-----------------------')            
            
            with open("netdevops_cicd/loopback_update_cicd/netconf_loopback.xml", "r") as file:
                config_data = file.read()
            print(config_data)
            print('--------------------(2)-----------------------')

            netconf_reply = m.edit_config(target='running', config=config_data)
            print(netconf_reply)

    except Exception as e:
        print(f"Erro de conexão: {e}")
        print('--------------------(1)-----------------------')

if __name__ == '__main__':
    main()


import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from device_info import ios_xe_sandbox
from ncclient import manager

# Função para carregar o conteúdo do arquivo de configuração
def config(file_path):
    full_path = os.path.abspath(os.path.join(os.path.dirname(__file__), file_path))
    with open(full_path, 'r') as file:
        return file.read()

if __name__ == '__main__':
    try:
        with manager.connect(
            host=ios_xe_sandbox['address'],
            port=ios_xe_sandbox['netconf_port'],
            username=ios_xe_sandbox['username'],
            password=ios_xe_sandbox['password'],
            hostkey_verify=False
        ) as m:
            print("Conexão bem-sucedida")
            print('--------------------(1)-----------------------')
            
            # Ler o arquivo de configuração
            config_data = config('loopback_config.xml')
            print(config_data)
            print('--------------------(2)-----------------------')

            # Enviar a configuração ao dispositivo
            netconf_reply = m.edit_config(target='running', config=config_data)
            print(netconf_reply)
            print('--------------------(3)-----------------------')

    except Exception as e:
        # Capturar e exibir qualquer erro de conexão
        print(f"Erro de conexão: {e}")
        print('--------------------(1)-----------------------')

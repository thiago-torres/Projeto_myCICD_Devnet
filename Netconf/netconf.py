import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from device_info import ios_xe
from ncclient import manager

# Função para carregar o conteúdo do arquivo de configuração
def config(file_path):
    with open(file_path, 'r') as file:
        return file.read()

if __name__ == '__main__':
    try:
        # Estabelecer conexão NETCONF com o dispositivo
        with manager.connect(
            host=ios_xe['address'],
            port=ios_xe['netconf_port'],
            username=ios_xe['username'],
            password=ios_xe['password'],
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

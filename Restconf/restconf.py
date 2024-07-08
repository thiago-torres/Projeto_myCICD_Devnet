import sys
import os
import json
import requests
from requests.auth import HTTPBasicAuth

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from device_info import ios_xe

# Função para carregar o conteúdo do arquivo de configuração JSON
def load_config(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

if __name__ == '__main__':
    print('--------------------(1)-----------------------')

    # URL base para o endpoint RESTCONF
    restconf_url = f"https://{ios_xe['address']}:{ios_xe['restconf_port']}/restconf/data"

    # Endpoint específico para configuração da interface Loopback
    loopback_url = f"{restconf_url}/Cisco-IOS-XE-native:native/interface/Loopback"

    # Headers necessários para o RESTCONF
    headers = {
        "Accept": "application/yang-data+json",
        "Content-Type": "application/yang-data+json"
    }

    # Carrega a configuração do arquivo JSON
    config_data = load_config('loopback_config.json')
    
    # Adiciona a descrição à configuração da interface
    config_data['Cisco-IOS-XE-native:Loopback']['description'] = "Configurado via Restconf - Thiago Torres"

    print(config_data)
    print('--------------------(2)-----------------------')

    # Realiza a autenticação básica usando as credenciais fornecidas
    auth = HTTPBasicAuth(ios_xe['username'], ios_xe['password'])
    
    response = requests.patch(loopback_url, json=config_data, headers=headers, auth=auth, verify=False)

    if response.status_code == 204:
        print("Configuração modificada com sucesso.")
    else:
        print(f"Falha ao modificar a configuração: {response.status_code} - {response.text}")

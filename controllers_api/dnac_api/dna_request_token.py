import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from device_info import dna_sandbox
from requests.auth import HTTPBasicAuth

import requests


def main():

    url = f"https://{dna_sandbox["address"]}:{dna_sandbox["port"]}/dna/system/api/v1/auth/token"
    print(f"URL being requested: {url}")
    auth = HTTPBasicAuth(dna_sandbox['username'], dna_sandbox['password'])
    
    response = requests.post(url, auth=auth, verify=False)  # O parâmetro verify=False ignora a verificação do certificado SSL
    
    if response.status_code == 200:
        token = response.json()["Token"]
        print(f"Token obtido: {token}")
    else:
        print(f"Falha ao obter o token. Status Code: {response.status_code}")
        print(f"Resposta: {response.text}")

if __name__ == "__main__":
    main()
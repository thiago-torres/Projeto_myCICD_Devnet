import os
import requests
from requests.auth import HTTPBasicAuth

def main():

    url = f"https://{os.getenv('DNA_ADDRESS')}:443/dna/system/api/v1/auth/token"
    print(f"URL being requested: {url}")
    auth = HTTPBasicAuth(os.getenv('DNA_USERNAME'), os.getenv('DNA_PASSWORD'))
    
    response = requests.post(url, auth=auth, verify=False)  # O parâmetro verify=False ignora a verificação do certificado SSL
    
    if response.status_code == 200:
        token = response.json()["Token"]
        print(f"Token obtido: {token}")
    else:
        print(f"Falha ao obter o token. Status Code: {response.status_code}")
        print(f"Resposta: {response.text}")

if __name__ == "__main__":
    main()
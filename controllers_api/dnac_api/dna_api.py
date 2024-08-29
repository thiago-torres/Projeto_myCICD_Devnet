import os
import requests
from requests.auth import HTTPBasicAuth

class DNAapi():
    def __init__(self):
        self.dna_addres = os.getenv('DNA_ADDRESS')
        self.dna_port = 443
        self.auth = HTTPBasicAuth(os.getenv('DNA_USERNAME'), os.getenv('DNA_PASSWORD'))

        self.token = self.token_request()
        self.headers = self.headers_request()

    def token_request(self):
        url = f"https://{self.dna_addres}:{self.dna_port}/dna/system/api/v1/auth/token"    

        try:
            response = requests.post(url, auth=self.auth, verify=False)  # O parâmetro verify=False ignora a verificação do certificado SSL
            
            if response.status_code == 200:
                token = response.json().get("Token")
                return token
            else:
                print(f"Falha ao obter o token. Status Code: {response.status_code}")
                print(f"Resposta: {response.text}")
                return None
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            return None

    def headers_request(self):
        if self.token:  
            headers = {
                    'x-auth-token': self.token,
                    'Content-Type': 'application/json'
                }
            return headers        
        else:
            self.headers = None
            print("Token inválido. Não foi possível definir os cabeçalhos.")

    def get_device_list(self):
        url = f'https://{self.dna_addres}:{self.dna_port}/dna/intent/api/v1/network-device'

        # Caso precisar filtrar da para usar params como lista

        try:
            response = requests.get(url=url, headers=self.headers, verify=False)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print(f"Erro: {response.status_code}")
                print(response.text)
                return None

        except Exception as e:
            print(f"Ocorreu um erro: {e}")

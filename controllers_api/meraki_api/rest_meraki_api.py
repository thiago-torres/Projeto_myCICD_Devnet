import os
import requests

class MerakiAPI:
    def __init__(self):
        self.api_key = os.getenv('MERAKI_API_KEY')        
        if not self.api_key:
            raise ValueError('A chave da API Meraki não está definida na variável de ambiente.')
        self.base_url = "https://api.meraki.com/api/v1"
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Cisco-Meraki-API-Key": self.api_key
        }

    def get_organizations(self):
        try:
            response = requests.get(f"{self.base_url}/organizations", headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao obter organizações: {e}")
            return None

    def get_networks(self, organization_id):
        try:
            response = requests.get(f"{self.base_url}/organizations/{organization_id}/networks", headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao obter redes: {e}")
            return None

    def get_devices(self, network_id):
        try:
            response = requests.get(f"{self.base_url}/networks/{network_id}/devices", headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao obter dispositivos: {e}")
            return None

    def get_admin(self, organization_id):
        try:
            response = requests.get(f"{self.base_url}/organizations/{organization_id}/admins", headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao obter admins: {e}")
            return None
    
    def get_alerts_profiles(self, organization_id):
        try:
            response = requests.get(f"{self.base_url}/organizations/{organization_id}/alertProfiles", headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao obter perfis de alerta: {e}")
            return None
    
    def get_alerts_settings(self, network_id):
        try:
            response = requests.get(f"{self.base_url}/networks/{network_id}/alerts/settings", headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao obter configurações de alerta: {e}")
            return None

    def get_inventory_devices(self, organization_id):
        try:
            response = requests.get(f"{self.base_url}/organizations/{organization_id}/inventory/devices", headers=self.headers, params={'perPage': 1000})
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao obter dispositivos do inventário: {e}")
            return None            

    def post_create_organization_admin(self, organization_id, email, name, org_access, authentication_method, tags=None, networks=None):
        try:
            payload = {
                "email": email,
                "name": name,
                "orgAccess": org_access,
                "authenticationMethod": authentication_method,
                "tags": tags,
                "networks": networks
            }
            response = requests.post(f"{self.base_url}/organizations/{organization_id}/admins", headers=self.headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao criar admin: {e}")
            return None


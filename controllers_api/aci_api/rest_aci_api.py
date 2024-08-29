import os
import requests

class ACIapi():
    def __init__(self):
        self.aci_address = os.getenv('ACI_ADDRESS')
        self.session = self.request_cookie()

    def request_cookie(self):
        url = f"https://{self.aci_address}:443/api/aaaLogin.json"
        headers = {'Content-type': 'application/json'}
        body = {
            "aaaUser": {
                "attributes": {
                    "name": os.getenv('ACI_USERNAME'),
                    "pwd": os.getenv('ACI_PASSWORD')
                }
            }
        }

        session = requests.Session()                                               
        response = session.post(url=url, headers=headers, json=body, verify=False)

        if response.status_code == 200:
            return session
        else: f"Error request cookie {None}"
    
    def request_tenant(self):
        tenant_url = f"https://{self.aci_address}:443/api/node/class/fvTenant.json"
        tenant_response = self.session.get(tenant_url, verify=False)
        return tenant_response
import os
import requests

def main():
    url = f"https://{os.getenv('ACI_ADDRESS')}:443/api/aaaLogin.json"
    headers = {'Content-type': 'application/json'}
    body = {
        "aaaUser": {
            "attributes": {
                "name": os.getenv('ACI_USERNAME'),
                "pwd": os.getenv('ACI_PASSWORD')
            }
        }
    }
    
    session = requests.Session()                                                #### Dessa forma o cookie será utilizado
    response = session.post(url=url, headers=headers, json=body, verify=False)  #### nas próximas requisições conforme abaixo
    
    print(f"Login Response: {response.status_code}")
    
    tenant_url = f"https://{os.getenv('ACI_ADDRESS')}:443/api/node/class/fvTenant.json"
    tenant_response = session.get(tenant_url, verify=False)
    
    print(f"Tenant Request Response: {tenant_response.json()}")

if __name__ == "__main__":
    main()


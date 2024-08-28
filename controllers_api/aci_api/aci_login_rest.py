import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
from device_info import aci_sandbox

def main():
    url = f"https://{aci_sandbox['address']}:{aci_sandbox['port']}/api/aaaLogin.json"
    headers = {'Content-type': 'application/json'}
    body = {
        "aaaUser": {
            "attributes": {
                "name": aci_sandbox["username"],
                "pwd": aci_sandbox["password"]
            }
        }
    }

    response = requests.post(url=url, headers=headers, json=body, verify=False)

    print(response.json())  

if __name__ == "__main__":
    main()

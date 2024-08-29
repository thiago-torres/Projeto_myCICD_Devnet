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

    response = requests.post(url=url, headers=headers, json=body, verify=False)

    print(response.json())  

if __name__ == "__main__":
    main()

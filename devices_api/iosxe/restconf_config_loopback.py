import os
import json
import requests
from requests.auth import HTTPBasicAuth

def main():
    print('--------------------(1)-----------------------')

    with open("restconf_loopback.json", 'r') as file:
        config_data = json.load(file)

    print(config_data)
    print('--------------------(2)-----------------------')
 
    url = f'https://{os.getenv("IOS_XE_ADDRESS")}:443/restconf/data'
    loopback_url = f"{url}/Cisco-IOS-XE-native:native/interface/Loopback"
    headers = {
        "Accept": "application/yang-data+json",
        "Content-Type": "application/yang-data+json"
    }
    auth = HTTPBasicAuth(os.getenv("IOS_XE_USERNAME"), os.getenv("IOS_XE_PASSWORD"))

    response = requests.patch(loopback_url, json=config_data, headers=headers, auth=auth, verify=False)

    if response.status_code == 204:
        print("Configuration successfully modified.")
    else:
        print(f"Failed to modify configuration: {response.status_code} - {response.text}")

if __name__ == "__main__":
    main()

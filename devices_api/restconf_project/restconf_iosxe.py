import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from device_info import ios_xe_sandbox
import json
import requests
from requests.auth import HTTPBasicAuth

def main():
    print('--------------------(1)-----------------------')

    config_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'loopback_config.json'))

    with open(config_file_path, 'r') as file:
        config_data = json.load(file)

    config_data['Cisco-IOS-XE-native:Loopback']['description'] = "Configured via Restconf - Thiago Torres - CICD Pipeline"

    print(config_data)
    print('--------------------(2)-----------------------')

 
    url = f"https://{ios_xe_sandbox['address']}:{ios_xe_sandbox['restconf_port']}/restconf/data"
    loopback_url = f"{url}/Cisco-IOS-XE-native:native/interface/Loopback"
    headers = {
        "Accept": "application/yang-data+json",
        "Content-Type": "application/yang-data+json"
    }
    auth = HTTPBasicAuth(ios_xe_sandbox['username'], ios_xe_sandbox['password'])

    response = requests.patch(loopback_url, json=config_data, headers=headers, auth=auth, verify=False)

    if response.status_code == 204:
        print("Configuration successfully modified.")
    else:
        print(f"Failed to modify configuration: {response.status_code} - {response.text}")

if __name__ == "__main__":
    main()

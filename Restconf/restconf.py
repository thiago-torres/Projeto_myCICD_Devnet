import sys
import os
import json
import requests
from requests.auth import HTTPBasicAuth

# Add parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from device_info import ios_xe

def load_json_config(file_path):
    full_path = os.path.abspath(os.path.join(os.path.dirname(__file__), file_path))
    with open(full_path, 'r') as file:
        return json.load(file)

def get_restconf_url(base_address, port):
    return f"https://{base_address}:{port}/restconf/data"

def get_loopback_url(base_url):
    return f"{base_url}/Cisco-IOS-XE-native:native/interface/Loopback"

def configure_loopback_interface(config_data, url, headers, auth):
    return requests.patch(url, json=config_data, headers=headers, auth=auth, verify=False)

def main():
    print('--------------------(1)-----------------------')

    restconf_url = get_restconf_url(ios_xe['address'], ios_xe['restconf_port'])
    loopback_url = get_loopback_url(restconf_url)

    headers = {
        "Accept": "application/yang-data+json",
        "Content-Type": "application/yang-data+json"
    }

    config_data = load_json_config('loopback_config.json')
    config_data['Cisco-IOS-XE-native:Loopback']['description'] = "Configured via Restconf - Thiago Torres - CICD Pipeline"

    print(config_data)
    print('--------------------(2)-----------------------')

    auth = HTTPBasicAuth(ios_xe['username'], ios_xe['password'])
    response = configure_loopback_interface(config_data, loopback_url, headers, auth)

    if response.status_code == 204:
        print("Configuration successfully modified.")
    else:
        print(f"Failed to modify configuration: {response.status_code} - {response.text}")

if __name__ == "__main__":
    main()

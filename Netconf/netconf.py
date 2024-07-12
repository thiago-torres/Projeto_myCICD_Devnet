import sys
import os
from ncclient import manager
from device_info import ios_xe

# Add parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def load_config(file_path):
    full_path = os.path.abspath(os.path.join(os.path.dirname(__file__), file_path))
    with open(full_path, 'r') as file:
        return file.read()

def connect_to_device():
    return manager.connect(
        host=ios_xe['address'],
        port=ios_xe['netconf_port'],
        username=ios_xe['username'],
        password=ios_xe['password'],
        hostkey_verify=False
    )

def send_config_to_device(connection, config_data):
    return connection.edit_config(target='running', config=config_data)

def main():
    try:
        with connect_to_device() as connection:
            print("Connection successful")
            print('--------------------(1)-----------------------')
            
            config_data = load_config('loopback_config.xml')
            print(config_data)
            print('--------------------(2)-----------------------')

            netconf_reply = send_config_to_device(connection, config_data)
            print(netconf_reply)
            print('--------------------(3)-----------------------')

    except Exception as error:
        print(f"Connection error: {error}")
        print('--------------------(1)-----------------------')

if __name__ == "__main__":
    main()

import sys
import os
from netmiko import ConnectHandler

# Add parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from device_info import ios_xe

def get_device_connection_params():
    return {
        'device_type': 'cisco_ios',
        'ip': ios_xe['address'],
        'username': ios_xe['username'],
        'password': ios_xe['password'],
        'port': ios_xe['ssh_port'],
        'secret': '',
        'verbose': False 
    }

def read_config_file(config_file_path):
    with open(config_file_path) as config_file:
        return config_file.read().splitlines()

def configure_device(connection, config_commands):
    return connection.send_config_set(config_commands)

def main():
    device_params = get_device_connection_params()
    connection = ConnectHandler(**device_params)

    config_file_path = os.path.join(os.path.dirname(__file__), 'loopback_config.txt')
    config_commands = read_config_file(config_file_path)

    config_output = configure_device(connection, config_commands)
    print("Configuration Output:\n", config_output)

    connection.disconnect()

if __name__ == "__main__":
    main()

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from device_info import ios_xr_sandbox
from netmiko import ConnectHandler

def main():
    # Definindo parâmetros de conexão
    device_params = {
        'device_type': 'cisco_ios',
        'host': ios_xr_sandbox['address'],
        'username': ios_xr_sandbox['username'],
        'password': ios_xr_sandbox['password'],
        'port': ios_xr_sandbox['ssh_port'],
        'secret': '',
        'verbose': False
    }

    connection = ConnectHandler(**device_params)

    with ConnectHandler(**device_params) as connection:
        config_file_path = os.path.join(os.path.dirname(__file__), 'loopback_config.txt')
        with open(config_file_path) as config_file:
            config_commands = config_file.read().splitlines()

        config_output = connection.send_config_set(config_commands)
        print("Configuration Output:\n", config_output)

if __name__ == "__main__":
    main()

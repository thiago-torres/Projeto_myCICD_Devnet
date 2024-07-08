import sys
import os
from netmiko import ConnectHandler

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from device_info import ios_xe

device = {
    'device_type': 'cisco_ios',
    'ip': ios_xe['address'],
    'username': ios_xe['username'],
    'password': ios_xe['password'],
    'port': ios_xe['ssh_port'],         
    'secret': '',        # Optional, in case of enable password
    'verbose': False     # Optional, set to True for verbose logs
}

connection = ConnectHandler(**device)

# Configurações a serem enviadas
config_file_path = os.path.join(os.path.dirname(__file__), 'loopback_config.txt')
with open(config_file_path) as config_file:
    config_commands = config_file.read().splitlines()

# Envia as configurações
config_output = connection.send_config_set(config_commands)
print("Saída das configurações:\n", config_output)

# Fecha a conexão
connection.disconnect()
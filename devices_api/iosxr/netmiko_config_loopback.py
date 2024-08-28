import os
from netmiko import ConnectHandler

def main():
    device_params = {
        'device_type': 'cisco_ios',
        'host': os.getenv("IOS_XR_ADDRESS"),
        'username': os.getenv("IOS_XR_USERNAME"),
        'password': os.getenv("IOS_XR_PASSWORD"),
        'port': 22,
        'secret': '',
        'verbose': False
    }

    print(device_params)

    connection = ConnectHandler(**device_params)

    with ConnectHandler(**device_params) as connection:
        with open("netmiko_loopback.txt") as file:
            config_data = file.read().splitlines()

        config_output = connection.send_config_set(config_data)
        print("Configuration Output:\n", config_output)

if __name__ == "__main__":
    main()

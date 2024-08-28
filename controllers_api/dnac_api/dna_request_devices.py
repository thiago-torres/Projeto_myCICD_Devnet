import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from device_info import dna_sandbox

from dna_api import DNAapi

def main():
    api = DNAapi(dna_sandbox)
    
    get_devices = api.get_device_list()
    for device in get_devices['response']:
        print('------------------------------------------------')
        print("Device: ")
        for key,value in device.items():
            print(f'{key} = {value}')

    print('------------------------------------------------')

if __name__ == "__main__":
    main()
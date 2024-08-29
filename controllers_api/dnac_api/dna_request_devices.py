from dna_api import DNAapi

def main():
    api = DNAapi()
    
    get_devices = api.get_device_list()
    for device in get_devices['response']:
        print('------------------------------------------------')
        print("Device: ")
        for key,value in device.items():
            print(f'{key} = {value}')

    print('------------------------------------------------')

if __name__ == "__main__":
    main()
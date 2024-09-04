from rest_meraki_api import MerakiAPI

def main ():
    api = MerakiAPI()

    response = api.get_organizations()
    print(response)

if __name__ == "__main__":
    main()
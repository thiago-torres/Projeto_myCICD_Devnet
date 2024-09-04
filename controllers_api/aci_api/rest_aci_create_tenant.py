from rest_aci_api import ACIapi

def main():
    api = ACIapi()

    response = api.create_tenant("test_thiago")
    print(response)

if __name__ == "__main__":
    main()
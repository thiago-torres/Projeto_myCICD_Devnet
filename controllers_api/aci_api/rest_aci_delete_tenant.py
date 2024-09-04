from rest_aci_api import ACIapi

def main():
    api = ACIapi()

    response = api.delete_tenant("Heroes")
    print(response)

if __name__ == "__main__":
    main()
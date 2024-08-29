import json
from rest_aci_api import ACIapi

def main():
    api = ACIapi()
    response = api.request_tenant()

    tenants = response.json()['imdata']

    for tenant in tenants:
        print(json.dumps(tenant, indent=4))

if __name__ == "__main__":
    main()

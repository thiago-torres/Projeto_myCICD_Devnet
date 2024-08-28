import meraki
import os

class MerakiAPI:
    def __init__(self):
        self.api_key = os.getenv('MERAKI_API_KEY')        
        if not self.api_key:
            raise ValueError('A chave da API Meraki não está definida na variável de ambiente.')
        self.dashboard = meraki.DashboardAPI(self.api_key)

    def get_organizations(self):
        try:
            organizations = self.dashboard.organizations.getOrganizations()
            return organizations
        except Exception as e:
            print(f"Erro ao obter organizações: {e}")
            return None

    def get_networks(self, organization_id):
        try:
            networks = self.dashboard.organizations.getOrganizationNetworks(organization_id)
            return networks
        except Exception as e:
            print(f"Erro ao obter redes: {e}")
            return None

    def get_devices(self, network_id):
        try:
            devices = self.dashboard.networks.getNetworkDevices(network_id)
            return devices
        except Exception as e:
            print(f"Erro ao obter dispositivos: {e}")
            return None

    def get_admin(self, organization_id):
        try:
            admin_list = self.dashboard.organizations.getOrganizationAdmins(organization_id)
            return admin_list
        except Exception as e:
            print(f"Erro ao obter admins: {e}")
            return None
    
    def get_alerts_profiles(self, organization_id):
        try:
            alerts = self.dashboard.organizations.getOrganizationAlertsProfiles(organization_id)
            return alerts
        except Exception as e:
            print(f"Erro ao obter admins: {e}")
            return None
    
    def get_alerts_settings(self, network_id):
        try:
            alerts = self.dashboard.networks.getNetworkAlertsSettings(network_id)
            return alerts
        except Exception as e:
            print(f"Erro ao obter admins: {e}")
            return None

    def get_invetory_devices(self, organization_id):
        try:
            inventory = self.dashboard.organizations.getOrganizationInventoryDevices(organization_id, total_pages='all')
            return inventory
        except Exception as e:
            print(f"Erro ao obter admins: {e}")
            return None            

    def post_create_organization_admin(self, organization_id, email, name, org_access, authentication_method, tags=None, networks=None):
        try:
            create_admin = self.dashboard.organizations.createOrganizationAdmin(
                organizationId=organization_id,
                email=email,
                name=name,
                orgAccess=org_access,
                authenticationMethod=authentication_method,
                tags=tags,
                networks=networks
            )
            return create_admin
        except Exception as e:
            print(f"Erro ao criar admin: {e}")
            return None

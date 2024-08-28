import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
import requests
from device_info import nexus_2

username = nexus_2['username']
password = nexus_2['password']
ip_addr =  nexus_2['address']

payload = {
  "topSystem": {
    "attributes": {
      "name": "NXAPI_2_CLI"
    }
  }
}
def aaa_login(username, password, ip_addr):
    payload = {
        'aaaUser' : {
            'attributes' : {
                'name' : username,
                'pwd' : password
                }
            }
        }
    url = "http://" + ip_addr + "/api/aaaLogin.json"
    auth_cookie = {}
    response = requests.request("POST", url, data=json.dumps(payload), verify=False)
    if response.status_code == requests.codes.ok:
        data = json.loads(response.text)['imdata'][0]
        token = str(data['aaaLogin']['attributes']['token'])
        auth_cookie = {"APIC-cookie" : token}
    print ()
    print ("aaaLogin RESPONSE:")
    print (json.dumps(json.loads(response.text), indent=2))
    return response.status_code, auth_cookie

def aaa_logout(username, ip_addr, auth_cookie):
    payload = {
        'aaaUser' : {
            'attributes' : {
                'name' : username
                }
            }
        }
    url = "http://" + ip_addr + "/api/aaaLogout.json"
    response = requests.request("POST", url, data=json.dumps(payload),
                                cookies=auth_cookie)
    print ()
    print ("aaaLogout RESPONSE:")
    print (json.dumps(json.loads(response.text), indent=2))
    print ()
def post(ip_addr, auth_cookie, url, payload):
    response = requests.request("POST", url, data=json.dumps(payload),
                                cookies=auth_cookie)
    print ()
    print ("POST RESPONSE:")
    print (json.dumps(json.loads(response.text), indent=2))
    
if __name__ == '__main__':
    status, auth_cookie = aaa_login(username, password, ip_addr)
    if status == requests.codes.ok:
        url = "http://" + ip_addr + "/api/mo/sys.json"
        post(ip_addr, auth_cookie, url, payload)
        aaa_logout(username, ip_addr, auth_cookie)
#!/usr/bin/env python3
import requests
import json
import pprint

base_url = "https://ios-xe-mgmt.cisco.com"
username = "developer"
password = "C1sco12345"
port = 9443

#disable insecure warnings
requests.packages.urllib3.disable_warnings()
# https://<url>/restconf<resource><container><leaf><options>
# GET request for root URL for RESTCONF resources, can work with 'application/yang-data+xml'
headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}

# GET request for specific resources
interface = "GigabitEthernet1"
interface_url = base_url + ":" + str(port) + "/restconf/data/ietf-interfaces:interfaces/interface=" + interface

response = requests.get(interface_url, auth=(username, password), headers=headers, verify=False)
#raw result
print("*" * 10)
pprint.pprint(response.json())

#parse result
print("*" * 10)
print(response.json()['ietf-interfaces:interface']['ietf-ip:ipv4']['address'][0]['ip'])

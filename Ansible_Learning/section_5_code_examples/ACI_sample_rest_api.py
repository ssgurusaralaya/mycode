#!/usr/bin/env python3
# References:
# https://developer.cisco.com/learning/modules/intermediate-aci-prog/sbx-intermediate-aci-01_aci-api/step/1
# https://www.cisco.com/c/en/us/td/docs/switches/datacenter/aci/apic/sw/2-x/rest_cfg/2_1_x/b_Cisco_APIC_REST_API_Configuration_Guide/b_Cisco_APIC_REST_API_Configuration_Guide_chapter_010.html
# https://unofficialaciguide.com/2019/03/04/apic-authentication-with-python/
# 
# To disable urllib3 warning: 
# export PYTHONWARNINGS="ignore:Unverified HTTPS request"


# Follow https://github.com/CiscoDevNet/aci-learning-labs-code-samples to set up 
# baseline for APIC Sandbox
from credentials import *
import requests

AUTH_URL = URL + '/api/aaaLogin.json'
r = requests.post(AUTH_URL, json={
    "aaaUser":{"attributes":{"name":LOGIN,"pwd":PASSWORD}}}, 
    verify=False)
token = r.json()["imdata"][0]["aaaLogin"]["attributes"]["token"]
cookie = {'APIC-cookie':token}

QUERY_URL = URL + '/api/node/class/fvTenant.json?query-target-filter=eq(fvTenant.name,"Heroes")'
r_heroes = requests.get(QUERY_URL, cookies=cookie, verify=False)

print("Here is the result: ")
print(r_heroes.json()['imdata'][0]['fvTenant']['attributes']['dn'])


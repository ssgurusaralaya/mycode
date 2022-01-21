#!/usr/bin/env python3
"""
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<topology>
  <node1 name="iosv-1">
    <interface name="GigabitEthernet0/1">on</neighbor>
  </node1>
</topology>
"""
import xml.etree.ElementTree as ET
from netmiko import ConnectHandler
import pprint

# check XML file to see if iosv-1 G0/1 should be on or off
tree = ET.parse('/home/echou/LinkedIn_Learning/Infra_as_Code/topology.xml')
root = tree.getroot()
int_state = root[0][0].text

print(f"iosv-1 interface G0/1 state should be {int_state}")

# apply interface state to iosv1
iosv1_connect = ConnectHandler(device_type='cisco_ios', host='172.16.1.91',
                               username='cisco', password='cisco')
if int_state == 'on':
    output = iosv1_connect.send_config_set(['interface GigabitEthernet0/1', 'no shut'])
    pprint.pprint(output)
else:
    output = iosv1_connect.send_config_set(['interface GigabitEthernet0/1', 'shut'])
    pprint.pprint(output)

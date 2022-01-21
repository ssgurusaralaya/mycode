#!/usr/bin/env python
# Modified Example from https://github.com/DevNetSandbox/sbx_iosxe/blob/master/yang/netconf/get_hostname.py
from ncclient import manager
import sys
import xml.dom.minidom
import pprint

# the variables below assume the user is leveraging the
# always on sandbox.
HOST = 'ios-xe-mgmt.cisco.com'
# use the NETCONF port for your IOS-XE device
PORT = 10000
# use the user credentials for your IOS-XE device
USER = 'developer'
PASS = 'C1sco12345'


# create a main() method
def main():
    """
    Main method that retrieves the interface from config via NETCONF.
    """
    with manager.connect(host=HOST, port=PORT, username=USER,
                         password=PASS, hostkey_verify=False,
                         device_params={'name': 'default'},
                         allow_agent=False, look_for_keys=False) as m:

        # XML filter to issue with the get operation
        interface_filter = '''
                          <filter>
                             <interfaces>
                               <interface><name>GigabitEthernet1</name></interface>
                             </interfaces>
                          </filter>
                          '''
        result = m.get_config('running', interface_filter)
        xml_doc = xml.dom.minidom.parseString(result.xml)
        #raw result
        print("*" * 10)
        print(xml_doc.toprettyxml())
        print("*" * 10)
        ip = xml_doc.getElementsByTagName("ip")
        print(ip[0].firstChild.nodeValue)


if __name__ == '__main__':
    sys.exit(main())

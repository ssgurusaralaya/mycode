import csv
import sys
import logging
import os  
from getpass import getpass
from netmiko import Netmiko
from netmiko import ConnectHandler
def main():
# open file "cisco.csv" and extract the two fields
    hosts_file="cisco.csv"
    with open("cisco.csv","r") as devicesfile:
       fields = ['hostname','devtype']
       hosts = csv.DictReader(devicesfile,fieldnames=fields,delimiter=',')
# iterate through list of hosts, 
# for each one
       for host in hosts:
           hostname = host["hostname"]
           print ('hostname = ' +  hostname)
           devtype = host['devtype']
           login_switch(hostname,devtype)
# import required module
# login into switch and run command
def login_switch(host,devicetype):
# required arguments to ConnectHandler
    device = {
# device_type and ip are read from data file
    'device_type': devicetype,
    'ip':host,
# device credentials are hardcoded in script for now
    "username": "cisco",
    "password": "cisco",
    }
# if successful login, use "config_changes.txt" fiels to run command on CLI
    cfg_file = "config_changes.txt"
    with ConnectHandler(**device) as net_connect:
        output = net_connect.send_config_from_file(cfg_file)
        output += net_connect.save_config()
    print()
    print(output)
    print("_______________________________________________________________")
    print("***************************************************************")
    try:
# Create a Directory in C Drive "changes"
# construct directory path based on device name
       path = '/changes/' + host + "/"
#    os.makedirs (path)
       filename = path + "Config diff"
# store output of command in file
       handle = open (filename,'a')
       handle.write(output)
       handle.close()
# if unsuccessful, print error
    except Exception as e:
        print  ("RAN INTO ERROR")
        print  ("Error: " + str(e))
import logging
if __name__ == "__main__":
    #  logging.basicConfig(level=logging.DEBUG)
    main()

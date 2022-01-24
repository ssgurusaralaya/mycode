from netmiko import ConnectHandler
ios = {
'device_type': 'cisco_ios',
'ip': '10.0.1.51',
'username': 'cisco',
'password': 'cisco'
}
net_connect = ConnectHandler(**ios)
output = net_connect.send_command('show ip int brief')
print (output)
config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print (output)

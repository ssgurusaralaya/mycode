from napalm import get_network_driver
driver = get_network_driver('ios')
ios = driver('10.0.1.51', 'cisco', 'cisco')
ios.open()
ios_output = ios.get_facts()
print (ios_output)

ios = driver('10.0.1.52', 'cisco', 'cisco')
ios.open()
ios_output = ios.get_facts()
print (ios_output)

ios = driver('10.0.1.53', 'cisco', 'cisco')
ios.open()
ios_output = ios.get_facts()
print (ios_output)

ios = driver('10.0.1.54', 'cisco', 'cisco')
ios.open()
ios_output = ios.get_facts()
print (ios_output)


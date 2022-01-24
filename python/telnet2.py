import telnetlib
import time
username = ("cisco")
password = ("cisco")
tn = telnetlib.Telnet("10.0.1.54")
tn.read_until("Username: ")
tn.write(username + "\n")
tn.read_until("Password: ")
tn.write(password + "\n")
tn.write("conf t\n")
time.sleep(1)

for x in range (2,10):
 tn.write("vlan " + str(x) + "\n")
 time.sleep(1)
 tn.write("name vlan_" + str(x) + "\n")
 time.sleep(1)

tn.write("end\n")
time.sleep(1)
tn.write("exit\n")

print (tn.read_very_eager())
print("\nThank You")

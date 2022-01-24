

import telnetlib
import time


username=("cisco")
password=("cisco")


tn = telnetlib.Telnet("10.0.1.51")
tn.read_until
tn.write(username+ "\n")
tn.read_until
tn.write(password + "\n")
tn.write("conf t \n")
time.sleep(1)
tn.write("interface loopback10 \n")
time.sleep(1)
tn.write("ip address 10.1.1.1 255.255.255.0 \n")
time.sleep(1)
tn.write("end \n")
time.sleep(1)
tn.write("exit \n")

print tn.read_very_eager()
print("\nThank You")


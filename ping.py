import sys
import os
hostname = "0.0.0.0"
interface = "eth0"
try:
    while True:
        response = os.system("ping -c 1 -I " + interface + " " + hostname)
        if response == 0:
		  print("Connection up! (;")
		else:
		  print("Connection down... );")
except KeyboardInterrupt:
pass

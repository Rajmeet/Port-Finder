
#Portscanner.py
import socket
import subprocess
import sys
from datetime import datetime

#Clear the screen
subprocess.call('clear', shell=True)

#Ask for input
remoteserver = str(input("Enter remote host to scan: "))
remoteServerIP = remoteserver

#Print a nice banner with information on which host we are about to scan
print("-" * 60)
print("Please wait, scanning remote host: ", remoteServerIP)
print("-" * 60)

#check the time the scan started
t1 = datetime.now()

#Using the range function to specify ports(here it will scan all ports between 1 and 1040)
#We also put in some error handling and catching for errors
try:
    for port in range(1,1040):
        print(port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP,port))
    if result == 0:
        print('Port {}: \t Open'.format(port))
        sock.close()
except Keyboardinterrupt:
    print("You pressed CTRL + C")
    sys.exit()
except socket.galerror:
    print("Hostname could not be resolved. Exiting...")
except socket.error:
    print("Couldn't connect to server. Exiting...")
    sys.exit()

#Check the time again
t2 = datetime.now()

#Calculate total time; subtract start time from end time
total = t2 -t1

#Print the total time on screen
print('\n')
print('-' * 60)
print("Open Ports: ", result)
print("Total scan time: ", total)
print('-' * 60)

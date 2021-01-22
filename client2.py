#!/usr/bin/python

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

print("connecting to {host} on port {port}")
#s.connect((host, port))
## si dovrebbe essere connesso, insierire
## qui il codice per elaborazioni dati da
## parte del client





## chiusura socket
s.close()
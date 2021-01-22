#!/usr/bin/python
import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)
while True:
    ## quando un client si connette viene 
    ## creato un nuovo socket (c) in una
    ## nuova porta non specificata (addr)
    c, addr = s.accept()


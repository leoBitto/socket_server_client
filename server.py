#!/usr/bin/python

import socket

s = socket.socket()
host = socket.gethostname()
port = 12346
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print("connection with", addr)
    c.send('thank you for connecting')
    c.close()
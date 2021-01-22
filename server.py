#!/usr/bin/python

import socket

s = socket.socket()
host = socket.gethostname()
print(s)
print(host)
port = 12345
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print(c)
    print(addr)
    c.send('thank you for connecting')
    c.close()
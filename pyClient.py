#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostname()
PORT = 1234

s.connect((HOST,PORT))

##### il client ha tentato di connettersi 
##### qui sotto può mandare richieste al server


##### chiude il socket
s.close()
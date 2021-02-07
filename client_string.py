#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostname()
PORT = 1234

s.connect((HOST,PORT))

##### il client ha tentato di connettersi 
##### qui sotto può mandare richieste al server
phrase = " today is a  "
s.send(phrase.encode())
completed_phrase = s.recv(1024).decode()
print(completed_phrase)

##### chiude il socket
s.close()
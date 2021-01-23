#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345

print(f"client: connecting to {host} on port {port}")

s.connect((host, port))
## si dovrebbe essere connesso, insierire
## qui il codice per elaborazioni dati da
## parte del client
print(f"client: just connected from {s.getsockname()}")
print("client: just sent a message to the server")
message = 'I am a string all over the network! Hello world!'
s.send(message.encode())


server_message = s.recv(1024).decode()
print(f"client: the server said: {server_message}")


## chiusura socket
s.close()
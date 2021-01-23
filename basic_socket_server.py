#!/usr/bin/env python3

import socket 

host = socket.gethostname()
port = 12345
print(f"server: waiting for client on port {port}")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()
    
while True:
    listening_socket, addr = s.accept()
    print(f"just connected to {addr}")
    message = f"Thank you for connecting to {host}"
    listening_socket.send(message.encode())
    listening_socket.close()
s.close()
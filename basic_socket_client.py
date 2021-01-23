#!/usr/bin/env python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
host = socket.gethostname()

s.connect((host, port))
print(f"client: connected_socket {host} on port {port}")
message = f"Hello from {socket.gethostname()}"
s.send(message.encode())
server_message = s.recv(1024).decode()
print(f"client: server said {server_message}")
s.close()
    

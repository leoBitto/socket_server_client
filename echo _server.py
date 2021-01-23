#!/usr/bin/python3
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
s.bind((host, port))
print(f"server: listening at {s.getsockname()}")
s.listen(5)
while True:
    ## quando un client si connette viene 
    ## creato un nuovo socket (c) in una
    ## nuova porta non specificata (addr)
    c, addr = s.accept()
    print(f"server: connected by {addr}")
    data = c.recv(1024)
    print(f"server: this is the data :{data}")
    if not data:
        print(f"server: ther is no data anymore")
        break
    #send data back to client
    c.sendall(data)
c.close()


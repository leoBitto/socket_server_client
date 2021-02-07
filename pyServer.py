#!/usr/bin/python3
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostname()
PORT = 1234
#BIND SOCKET
s.bind((HOST, PORT))
#SET SOCKET TO LISTENING
s.listen()
print(f"client: hostname: {socket.gethostname()}, 
                name in network: {socket.gethostbyname()")
#WORK LOOP
while True:
    listening_socket, addr = s.accept()
    print(f"client: the server name is {listening_socket.getpeername()}")
    print(f"client: the server addr is {addr}")
    ####### the server here can receive o send data to
    ####### connected client



####### the connection can be closed
listening_socket.close()
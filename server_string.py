#!/usr/bin/python3
import socket
import random
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostname()
PORT = 1234
#BIND SOCKET
s.bind((HOST, PORT))
#SET SOCKET TO LISTENING
s.listen()
#print(f"server: hostname: {socket.gethostname()}, name in network: {socket.gethostbyname(socket.gethostname())}")

words = ['good', 'sunny', 'wonderful']

#WORK LOOP
while True:
    listening_socket, addr = s.accept()
    #print(f"server: the client name is {listening_socket.getpeername()}")

    ####### the server here can receive o send data to
    ####### connected client
    message = listening_socket.recv(1024).decode()
    
    message += words[random.randint(0,2)]
    listening_socket.send(message.encode())


####### the connection can be closed
listening_socket.close()
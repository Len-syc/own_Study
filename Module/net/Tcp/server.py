from socket import *
import functools
from datetime import datetime

IP = '127.0.0.1'
PORT = 8080
BUFSIZ = 1024
listenSocket = socket(AF_INET, SOCK_STREAM)
listenSocket.bind((IP, PORT))
listenSocket.listen(5)
print(f'Server running on port {PORT}')

dataSocket, addr = listenSocket.accept()
print(f'Client connected from {addr}')

while True:
    recvData = dataSocket.recv(BUFSIZ)
    if not recvData:
        print(f'Client disconnected from {addr}')
        break
    info = recvData.decode()
    print(f'Client: {addr}|Message: {info}')
    dataSocket.send(f"{info} too".encode())
dataSocket.close()
listenSocket.close()
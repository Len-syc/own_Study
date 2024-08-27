from socket import *
import time
test = socket(AF_INET, SOCK_STREAM)
IP = '127.0.0.1'
PORT = 8080
try:
    test.connect((IP, PORT))
except ConnectionRefusedError:
    print('Connection refused')
    time.sleep(5)
    test.connect((IP, PORT))
while True:
    toSend = input(">>>")
    if toSend == "exit":
        break
    test.send(toSend.encode())
    data = test.recv(1024)
    if not data:
        break
    print(f"服务端：{IP}|消息：{data.decode()}")
test.close()
import socket
import random

serverName = 'localhost'
serverPort = 12000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))

while True:
    rand = random.randint(0, 10)

    message, addr = serverSocket.recvfrom(1024)
    
    message = message.upper()

    if rand < 4:
        continue
    serverSocket.sendto(message, addr)
    print(addr)
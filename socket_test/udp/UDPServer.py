import socket

serverPort = 12000
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

serverSocket.bind(('localhost', serverPort))

print('服务器已经启动')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print('收到的信息为：', message)
    print(clientAddress)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
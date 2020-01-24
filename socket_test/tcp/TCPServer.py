import socket

serverName = 'localhost'
serverPort = 10001

# 这个是欢迎套接字，负责处理tcp的初始连接
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
# 让欢迎套接字开始监听
serverSocket.listen()
print('服务器正在等待连接')

while True:
    # 欢迎套接字收到了连接，创建了一个连接套接字
    # 并且返回客户端的地址
    connectSocket, addr = serverSocket.accept()
    print('客户端的地址为：', addr)
    sentence = connectSocket.recv(1024).decode()
    modifiedSentence = sentence.upper()
    connectSocket.send(modifiedSentence.encode())
    # 关闭此连接
    connectSocket.close()
import socket

serverName = 'localhost'
serverPort = 10001
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 启动连接，进行三次握手
clientSocket.connect((serverName, serverPort))

sentence = input('请输入一些垃圾：')
# 发送数据，和UDP不同，因为已经建立了连接，不需要指定地址
clientSocket.send(sentence.encode())
# 回包
modifiedSentence = clientSocket.recv(1024)
print('从服务器返回的信息为：', modifiedSentence.decode())
# 关闭连接
clientSocket.close()
import socket

tcpWelSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpWelSocket.bind(('', 8001))
tcpWelSocket.listen(1)

# 开始接收请求
while True:
    print('开始接收请求')
    connectSocket, addr = tcpWelSocket.accept()
    print('接收到了来自',addr,'的请求')
    message = connectSocket.recv(4096).decode()
    if not message:
        continue

    # 提取出文件名
    fileName = message.split()[1].partition('//')[2].replace('/', '_')
    fileExis = False
    
    try:
        # 看一下文件是否已经存在缓存中
        f = open(fileName, 'r')
        fileExis = True
        print('缓存存在，将把缓存的文件发送过去')
        for line in f:
            connectSocket.send(line.encode())
    except IOError as e:
        print('没有缓存')
        print(e)
        # 建立一个新的tcp连接去获取原始服务器的文件
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        hostName = message.split()[1].partition("//")[2].partition("/")[0]
        try:
            print('开始连接到远程服务器')
            
            c.connect((hostName, 80))
            c.sendall(message.encode())
            print('发送数据到远程服务器，数据为：')
            print(message)
            
            buff = c.recv(4096)
            connectSocket.sendall(buff)

            print('开始缓存')
            
            with open(fileName, 'w') as f:
                f.write(buff.decode())
        except Exception as e:
            print('发生了一些不可预知的错误')
            print(e)
    else:
        print('悲惨！')
    connectSocket.close()
tcpWelSocket.close()
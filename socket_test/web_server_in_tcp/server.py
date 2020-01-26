import socket
import time

welcome = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
welcome.bind(('', 80))
welcome.listen(1)

while True:
    print('服务器正在监听')
    connectSocket, addr = welcome.accept()
    try:
        data = connectSocket.recv(1024)
        print(data)
        if not data:
            continue
        fileName = data.split()[1]
        print(fileName[1:].decode())
        f = open(fileName[1:].decode())
        fileData = f.read()
        # header 
        # mime
        fileType = ''
        if fileName.decode().find('css') > -1:
            fileType = 'css'
        elif fileName.decode().find('html') > -1:
            fileType = 'html'
        header = 'HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/%s\nContent-length: %d\n\n' % (fileType, len(fileData))
        connectSocket.send(header.encode())
        connectSocket.send(fileData.encode())

        # for i in range(0, len(fileData)):
        #     connectSocket.send(fileData[i].encode())
        #     connectSocket.close()
        
    except IOError:
        header = 'HTTP/1.1 404 Found'
        connectSocket.send(header.encode())
        print('哈哈哈')
    # finally:
    #     if f:
    #         f.close()

welcome.close()
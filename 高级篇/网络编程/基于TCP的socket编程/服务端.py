if __name__=='__main__':
    import socket   #创建socket对象
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('localhost',8001))         #绑定到本地的8001端口
    sock.listen(5)                        #在本地的8001端口监听,等待队列最长长度为5
    while True:
        connection,address=sock.accept()  #接收客户端的请求
        try:
            connection.settimeout(5)
            buf=connection.recv(1024).decode('utf-8')  #接收客户端的数据
                                                       #1024指定缓冲区大小
            if buf=='1':
                connection.send(b'welcome to server!')
            else:
                connection.send(b'please go out')
        except socket.timeout:
            print('time out')
        connection.close()

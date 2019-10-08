# -*- coding:utf-8 -*-
'''
服务器端编程:
服务器会打开固定端口（比如80）监听，
每来一个客户端连接，就创建该Socket连接。
由于服务器会有大量来自客户端的连接，
所以，服务器要能够区分一个Socket连接是和哪个客户端绑定的。
一个Socket依赖4项：服务器地址、服务

但是服务器还需要同时响应多个客户端的请求，
所以，每个连接都需要一个新的进程或者新的线程来处理，
否则，服务器一次就只能服务一个客户端了。
'''

import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5) # 指定等待连接的最大数量为5（即，最多五个线程同时等待）
print('Ready to work!')


# 工作函数
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s' % data.decode('utf-8')).encode('utf-8'))
    sock.close() # 接收完毕后关闭与对方的连接
    print('Connections from %s:%s closed.' % addr)

# 通过一个死循环，来等待来自客户端连接
while True:
    # 接受一个新连接
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()


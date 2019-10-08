# -*- coding:utf-8 -*-

'''
使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能到达就不知道了。

虽然用UDP传输数据不可靠，但它的优点是和TCP比，速度快，对于不要求可靠到达的数据，就可以使用UDP协议。
'''

import socket, time

# SOCK_DGRAM指定socket类型为UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))
# UDP不需要listen方法
print('Bind UDP on 9999...')
while True:
    # 接收数据 --> 接收来自任何客户端的数据
    data, addr = s.recvfrom(1024)
    time.sleep(1)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr) # 将数据添加个Hello发回去



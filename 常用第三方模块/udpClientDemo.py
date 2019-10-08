# -*- coding:utf-8 -*-

import socket

# 客户端无需连接，直接发送即可
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'xzxldl', b'xzx', b'ldl']:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据
    print(s.recv(1024).decode('utf-8'))
s.close()
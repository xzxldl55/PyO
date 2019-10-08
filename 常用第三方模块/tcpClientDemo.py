# -*- coding:utf-8 -*-
'''
tcp对应的客户端程序

'''
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(s.recv(1024).decode('utf-8')) # 接收欢迎消息
for data in [b'xzxldl55', b'xzx', b'ldl']:
    # 发送数据
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit') # 退出
s.close()
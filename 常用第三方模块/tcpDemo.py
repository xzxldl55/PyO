# -*- coding:utf-8 -*-
import socket

# 创建一个socket, AF_INET指定IPv4协议（IPv6为AF_INET6）， SOCK_STEAM指定使用面向流的TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('www.baidu.com', 80))
#发送请求(HTTP为客户端先发，服务端后发)
s.send(b'GET / HTTP/1.1\r\nHost:www.baidu.com\r\nConnetction: close\r\n\r\n')

# 接收数据
buffer = []
while True:
    # 每次至多接收1kb
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

# 关闭socket
s.close()

# 将头与网页内容分离
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 将网页数据写入文件
with open('baidu.html', 'wb') as f:
    f.write(html)


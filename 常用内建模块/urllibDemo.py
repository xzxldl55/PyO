# -*- coding:utf-8 -*-

'''
urllib提供了一系列操作url的方法
'''

# 1.Get：urllib的request模块能够方便的抓去URL内容，即发送一个GET请求到制定界面，然后等待HTTP响应
from urllib import request, parse
# with request.urlopen('http://www.baidu.com') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))

# 2.如果想要模仿浏览器请求发送GET，则需要使用Request对象，通过往Request中添加HTTP头，将请求伪装成浏览器
# req = request.Request('http://www.douban.com/')
# 模拟手机访问
# req.add_header('User-Agent', 'Moazilla/6.0 (iPhone; CUP iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))

# 3.POST则将data以bytes形式传入：
print('Login to weibo.cn...')
email = input('Email: ')
password = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', password),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])
req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status: ', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data: ', f.read().decode('utf-8'))

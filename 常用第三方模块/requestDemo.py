# -*- coding:utf-8 -*-

'''
requests 用于处理url资源，比urllib方便
'''
import requests

# 1.get访问(url, params, header, cookie, ....)
# rget = requests.get('http://www.baidu.com', params={'q': 'xzxldl', 'cat': '10010'}, header={}, timeout=2.5)
# print(rget.status_code)
# print(rget.text)

# 2.POST只需要将get方法变成post，且传入data参数即可
# 默认为application/x-www-form-urlencoded的数据编码（form表单）
cookieDict = { 'ts': '》？？为什么没东西', 'ts': '21001' }
rpost = requests.post('http://www.baidu.com', data={'msg': '传给你了，接不接受我不管'}, cookies=cookieDict)
# 若要传入Json数据，可以传入json参数，其内部会自动序列化为json
rpost2 = requests.post('http://www.xzxldl.github.io/api/jiade', json={'apiname': '反正只是我编的'})
# 上传文件哦：
upload_files = {'file': open('code.jpg', 'rb')}
rpostfile = requests.post('http://www.baidu.com/api/upload_img/', files=upload_files)
# 同理，还有put与delete一样的

# others: 响应头啊，cookie啊这些
print(rpostfile.headers['Content-Type'])
print(list(rpost.cookies))

# -*- coding:utf-8 -*-

'''
Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。

什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。

举个例子，你写了一篇文章，内容是一个字符串'how to use python hashlib - by Michael'，并附上这篇文章的摘要是'2d73d4f15c0db7f5ecb321b6a65e5d6d'。如果有人篡改了你的文章，并发表为'how to use python hashlib - by Bob'，你可以一下子指出Bob篡改了你的文章，因为根据'how to use python hashlib - by Bob'计算出的摘要不同于原始文章的摘要。

摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。
'''
import hashlib

# 1.md5：一般用于对登陆密码的加密，存储在数据库的也是md5加密后的str
md5 = hashlib.md5()
# md5.update('xzxldl55'.encode('utf-8'))
# print(md5.hexdigest())
# 数据量大时可以分多次调用update效果是一样的
# md5.update('xzx'.encode('utf-8'))
# md5.update('ldl'.encode('utf-8'))
# md5.update('55'.encode('utf-8'))
# print(md5.hexdigest())

# 2.SHA1：与md5调用方式完全一致，但其结果是160bit字节（md5为128bit）
# sha1 = hashlib.sha1()
# sha1.update('how to use sha1 in '.encode('utf-8'))
# sha1.update('python hashlib?'.encode('utf-8'))
# print(sha1.hexdigest())

'''
md5一般来说很安全了，但对于黑客来说，一般都会事先统计处一个常用密码
的md5映射表（所以要加强密码强度），而有映射表的情况下能够轻易找到md5对应的原密码

所以，一般来说，为了确保用户口令不是那些常用的，都会对原始口令“加盐”
即，再存储／查询前对用户口令进行添加eg：
def calc_md5(password):
    return get_md5(password + 'the-Salt')
'''

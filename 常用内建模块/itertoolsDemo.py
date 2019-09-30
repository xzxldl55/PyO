# -*- coding:utf-8 -*-

'''
内建模块itertools提供了非常有用的用于操作迭代对象的函数。
'''
import itertools

# 1.无限迭代器：
# 1⃣️count将创建一个无限迭代器，接收两个参数，起始值，步长
# natuals = itertools.count(1)
# for n in natuals:
#     print(n)
# 2⃣️cycle将会把传入的一个序列无限地重复下去
# cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)
# 3⃣️repeat能够将一个元素无限重复下去，如果提供第二个参数，则可重复有限次数
# ns = itertools.repeat('X', 3)
# for n in ns:
#     print(n)

# 4⃣️通常我们会通过takewhile()等函数根据条件判断来截取出一个有限序列
# 接受两个参数，第一个为filterFn，第二个为无限序列
# myns = itertools.takewhile(lambda x: x <= 10, natuals)
# print(list(myns))

# 2.chain()能够将一组迭代对象串联起来，形成一个更大的迭代器
# for c in itertools.chain('ABC', '123'):
#     print(c)

# 3.groupby()将迭代器中相邻的重复元素挑出放在一起，可接收第二个参数，对第一个参数的迭代器做处理（类似map）
# 此处将其转为大写，则dd也将和D分为一组
# for key, group in itertools.groupby('AAABBBCCCAAADddCSD', lambda c: c.upper()):
#     print(key, list(group))

# -*- coding:utf-8 -*-
'''
并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。
实现上下文管理是通过__enter__和__exit__这两个方法实现的。例如，下面的class实现了这两个方法：
'''


# class Query(object):
#     def __init__(self, name):
#         self.name = name

#     def __enter__(self):
#         print('Begin')
#         return self

#     def __exit__(self, exc_type, exc_value, taceback):
#         if (exc_type):
#             print('Error')
#         else:
#             print('End')

#     def query(self):
#         print('Query info about %s...' % self.name)


# 即可使用with语句
# with Query('Bob') as q:
#     q.query()

# 1.contextlib提供了简单的方法来避免便携__enter__ & __exit__的繁琐
from urllib.request import urlopen
from contextlib import contextmanager, closing


class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)
# 使用装饰器contextmanager来创建Query
@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')


# with首先执行yield前的语句，打印Begin，yield调用with内部的所有语句，最后执行yield之后的语句
# with create_query('Bob') as q:
#     q.query()

# 2.@closing：如果一个对象没有实现上下文，则无法使用with来调用。此时可以使用closing来将该对象变为上下文对象，例如用with使用urlopen()
with closing(urlopen('https://www.baidu.com')) as page:
    for line in page:
        print(line)

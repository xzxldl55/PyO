# -*- coding:utf-8 -*-

'''
当我们认为某些代码可能会出错时，
就可以用try来运行这段代码，
如果执行出错，则后续代码不会继续执行，
而是直接跳转至错误处理代码，即except语句块，
执行完except后，如果有finally语句块，
则执行finally语句块，至此，执行完毕。
'''
try:
  print 'try run'
  print 10 / 0
except ZeroDivisionError as e:
  print 'Error:', e
except ValueError as e:
  print 'ValueError:', e
finally: # 无论是否出错都会执行finally中的代码
  print 'Ok!'


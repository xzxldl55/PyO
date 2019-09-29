# -*- coding: utf-8 -*-

"Module's annotation"

__author__ = "Xzxldl55"

import sys

def test():
  args = sys.argv
  if len(args) == 1:
    print 'Hello World!'
  elif len(args) == 2:
    print('Hello, %s!' % args[1])
  else:
    print("enheng!")


## 一般来说，正常的函数/变量名在模块中都是public的，而当函数/变量名为_xx或__xx时，被视作private，不应被引用
## 但这只是习惯上的约束，Python并未提供完全限制private的访问。
## 而对于__xx__的变量则为特殊变量，有着特殊用途


# 当模块被别的文件导入时__name__ != '__main__'，只有在命令行执行该模块时，才会相等而运行其中代码
if __name__ == '__main__':
  test()
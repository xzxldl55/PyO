# -*- coding:utf-8 -*-
'''
Python内置的os模块也可以直接调用操作系统提供的接口函数:
'''
import os

# 1.操作系统类型：如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
# print(os.name) 

# 2.要获取详细的系统信息，可以调用uname()函数：(windows没有这个模块)
# print(os.uname())

# 3.在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
# print(os.environ)
# print(os.environ.get('PATH')) #要获取某个环境变量的值，可以调用os.environ.get('key')：

# 4.操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：
# print(os.path.abspath('.')) # 查看当前目录绝对路径

# 在某目录下，创建新目录
# os.path.join('D:/VueLearn/PythonLearn', 'testdirModule') #首先要吧新目录的完整路径表达出来
# os.mkdir('D:/VueLearn/PythonLearn/testdirModule') #接着创建目录
# os.rmdir('D:/VueLearn/PythonLearn/testdirModule') #删除一个目录
# print(os.path.splitext('./decorator.py')) # os.path.splitext()可直接得到文件的拓展名

# 5.文件操作
# os.rename('test.txt', 'test.py') # 修改文件名
# os.remove('test.txt') # 删除文件
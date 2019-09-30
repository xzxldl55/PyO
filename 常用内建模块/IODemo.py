# -*- coding:utf-8 -*-
import codecs

'''
1. 一般写法：即使用open直接打开文件，并为了捕获异常使用try...except...finally
  *注：python 3.0指定文件编码可直接在open第三个参数指定
  python 2.7并无该参数，需import codecs模块，使用codecs.open(filePath, mode, encoding)来实现
  其写入，亦然f.write(str.decode('utf-8'))
'''
# try:
#   f = open('./test.txt', 'r')
#   print f.read()
# except:
#   raise IOError(u'打不开啊')
# finally:
#   f.close()

'''
2. 但如此太为繁琐，即引入with语句以自动调用close()
  虽如此，然则文件过大，总不能期许每每只用read进行操作，所以有了read(size)以读取指定字节大小的内容
  或readline()读取一行内容，或readlines()以此读取所有内容，并按照行返回list
'''
# with codecs.open('./send.py', 'r', 'utf-8') as f:
#   print f.read()
#   for x in f.readlines():
#     print x

'''
3. file-like Object 即像open函数返回的有read()的对象。file-like Object不要求从特定类继承，只要写个read()方法就行。
'''

'''
4. 二进制文件读取，使用rb模式打开即可
'''
# with open('./lks.jpg', 'rb') as img:
#   print img.read()
  # print img.write(b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00')

'''
5. open第四个参数errors可设置为ignore表示忽略读取中的编码错误
'''

'''
6. 写文件：区别则在于调用open时mode为w或wb。
'''
with open('./test.txt', 'w') as w:
  w.write('你说我要多难堪？')

'''
7. Mode：共有12中mode，其为三种操作，每种操作有四个模式
r/rb/r+/rb+：只读文件，读二进制文件，从头开始读写文件(替换)，~
w/wb/w+/wb+：只写文件，~，文件存在则覆盖不存在重新创建，~写入内容为bytes
a/ab/a+/ab+：追加只写（内容追加到文件内容结尾），~，读写~，读写~
'''

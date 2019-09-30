# -*- coding:utf-8 -*-

'''
准确地讲，Python没有专门处理字节的数据类型。
但由于b'str'可以表示字节，所以，字节数组＝二进制str。
而在C语言中，我们可以很方便地用struct、union来处理字节，以及字节和int，float的转换。
'''
# 【引子】在Python中，比方说要把一个32位无符号整数变成字节，也就是4个长度的bytes，你得配合位运算符这么写：
# n = 10240099
# b1 = (n & 0xff000000) >> 24
# b2 = (n & 0xff0000) >> 16
# b3 = (n & 0xff00) >> 8
# b4 = n & 0xff
# bs = bytes([b1, b2, b3, b4])
# print(bs)  # '\x00\9c@c'

# 【正文】Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。

# 1.struct的pack函数将任意数据类型转换为bytes
import struct
# >I的意思为：‘>’表示字节顺序，I表示4字节无符号整数，第二个参数为值，需要与前一个参数匹配
# print(struct.pack('>I', 1024666))
# 将bytes数据转换为相应数据类型数据
# IH表示依次变为4字节无符号整数与2字节...
# print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))

# 2.

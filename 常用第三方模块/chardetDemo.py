# -*- coding:utf-8 -*-

'''
在不知道编码的情况下bytes与decode()并不好搞。
对于位置编码的bytes，想要将其转换为str，需要先猜测编码。
猜测的方式是事先收集各种编码的特征自负，根据特征自负判断就有很大概率能猜对。

基于此chardet派上用场了，它能用于检测编码方式。
'''
import chardet
print(chardet.detect(b'Hello, world!')) # --> ascii, confidence: 1.0即表示检出率100%

print(chardet.detect('静夜思，床前明月光，疑似地上霜。'.encode('gbk')))
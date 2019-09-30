# -*- coding:utf-8 -*-

'''
操作XML有两种方法：DOM和SAX:
    DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
    SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了。
    举个例子，当SAX解析器读到一个节点时：
    `<a href='/'>py</a>`
    会产生三个事件：
        1）start_element事件，在读取<a href='/'>时
        2）char_data事件，读取py时
        3）end_element事件，读取</a>时
'''

# -*- coding: utf-8 -*
from functools import reduce

# 1. 装饰器是一个我们希望能够在函数调用前后执行的函数，如日志打印，登录验证等
# （1）装饰器接受一个函数为参数，并在内部将其返回
# def _log(func):
#   def _log_name(*args, **kw):
#     print("func name is: %s" % func.__name__)
#     return func(*args, **kw)
#   return _log_name

# @_log # 相当于执行car_bus = _log(car_bus)，将函数放入_log中，用return执行
# def car_bus():
#   print("I'll say 'car_bus'")

# car_bus()


# （2）如果是一个需要接受参数的装饰器，则需要编写一个返回装饰器的高阶函数
# def _log2(text):
#   def decorator(func):
#     def _log_name2(*args, **kw):
#       print("func name is: %s, something is : %s" % (func.__name__, text))
#       return func(*args, **kw)
#     return _log_name2
#   return decorator # 该函数返回一个装饰器

# @_log2(u'嗯哼') # 实际执行为：car_bus2 = _log2(u'嗯哼')(car_bus2)
# def car_bus2():
#   print("I'll say 'car_bus'")
# car_bus2()

# 2. 可变参数 -- > 将在内部自动将参数组装成一个tuple
# def add(*numbers):
#   add = 0
#   for num in numbers:
#     add += num
#   return add
# nums = [0,1,2,3,4]
# print add(*nums) # 可变参数传入list可使用*
# print add(0,1,2,3,4) # 同上

# 3. 关键词参数，将多余参数组装成一个dict
# def keyword(a, b, **kw):
#   print("a is ", a, "b is ", b, "kw is ", kw)
# kw = {
#   "city": 'BeiJing',
#   "region": 'Chaoyang'
# }
# keyword("a", "b", **kw)
# keyword("a", "b", city="BeiJing", region="Chaoyang")
## **命名关键字参数，规定只接受该关键字名的参数
# def keyword2(a, b, * city, region):
## 由于这种机制，我们可以通过func(*args, **kw)来调用任何函数，而不论他的参数是如何定义的


# 4. 列表生成器[listItem(可为表达式) for key in keys for key2 in keys2 filter(如if key % 2 == 0过滤出偶数)]
# 5. 生成器，在Python中一边循环一边计算的机制，称为生成器：generator。可以在循环的过程中不断推算出后续的元素，这样就不必创建完整的list。
# g = (x*x for x in range(10)) generator元素获取能通过next()来一个一个获取：next(g) ...
# 当然，generator同样可以使用for进行迭代 for n in g
# 如，斐波那契数，函数的表达为：
# def fib(max):
#   n, a, b = 0, 0, 1
#   while n < max:
#     print b
#     a, b = b, a + b
#     n = n + 1
#   return 'done'
# fib(10)
# 使用generator，则只需将print改为yield，使用了yield的函数则将变成generator
# def fib2(max):
#   n, a, b = 0, 0, 1
#   while n < max:
#     yield b
#     a, b = b, a + b
#     n = n + 1
# f = fib2(10)

# 6. 高阶函数—map&reduce
## （1） map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
# mapList1 = [0, 1, 2, 3, 4, 5]
# def square(x):
#   return x * x
# mapList2 = map(square, mapList1)
# print mapList2

## （2）reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其中第一个参数是之前的结果，第二个参数为序列中下一个元素
##      使用reduce需要from functools import reduce
# def accumulation(x, y):
#   print 'x:', x, 'y:', y
#   return x * 10 + y
# reduceList = [1, 2, 3]
# print reduce(accumulation, reduceList)

## eg: str转int
# def strToIntArr(x):
#   try:
#     return int(x)
#   except:
#     pass

# def clearIntArr(arr):
#   brr = arr
#   n = len(brr) - 1
#   while n >= 0:
#     if type(brr[n]) != type(1):
#       brr.pop(n)
#     n -= 1
#   return brr

# def toInt(x, y):
#   return x * 10 + y

# print reduce(toInt, clearIntArr(map(strToIntArr, "123ab54")))

## 7.高阶函数：filter
### filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# def not_empty(s):
#     return s and s.strip()

# print list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))

## eg: 埃氏筛法筛取素数

# 生成奇数序列序列
# def _odd_iter():
#   n = 1
#   while True:
#     n = n + 2
#     yield n
# # 筛选器
# def _not_divisible(n):
#   return lambda x: x % n > 0
# # 生成器，返回下一个素数
# def primes():
#   yield 2
#   it = _odd_iter() # 初始序列
#   while True:
#     n = next(it) # 返回序列的第一个数
#     yield n
#     it = filter(_not_divisible(n), it) # 构造新序列

# for n in primes():
#   if 10 < 100:
#     print n
#   else:
#     break

# 8.匿名函数：lambda表达式，关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# print map(lambda x: x * x, [1, 2, 3, 4, 5])


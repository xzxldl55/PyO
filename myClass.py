# -*- coding:utf-8 -*-

'''
Python 2.7存在新式类与经典类之分，不手动继承object类时，是为“经典类”，反之为新式类（Python 3不必理会）
其中经典类在遍历寻找某方法时，采用深度优先方法，且诸如__solts__与@property等方法无效
而新式类采用广度优先，新式类拥有各种高级此特性，而经典类只有doc，module与自定义的属性三者而已
eg:
## 经典类
class A:
  def foo(self):
    print 'A-foo'

class B(A):
  pass

class C(A):
  def foo(self):
    print 'C-foo'

class D(B, C):
  pass

此时我们创建d为类D的实例，则d.foo将打印出'A-foo'而非'C-foo'，因为其为深度遍历
寻找的顺序为B-A-c
！反之，若A为新式类：
## 新式类
class A(object):
  def foo(self):
    print 'A-foo'

class B(A):
  pass

class C(A):
  def foo(self):
    print 'C-foo'

class D(B, C):
  pass

则此时d.foo 打印的是'C-foo'其广度遍历，顺序为B-C-A
从逻辑上来说D直接继承了C，所以应当是新式类的遍历方法更加隔离，
即一般推荐使用新式类，在Python 2.7中需记手动添加继承object类
'''

# · class 类名(继承自哪个类):
# class Student(object):
#   def __init__(self, name, score, age):
#     self.name = name
#     self.score = score
#     # 在属性名前加__表示为一个private属性（有实质性的保护）
#     self.__age = age 
#   def get_score(self):
#     return self.score

# · 实例化: 类名()
# Mike = Student('Xzxldl55', 90, 20)
# 可以自由的给实例对象，绑定任意属性（类中没有定义也行）,对于认为必须存在的属性，在类中定义__init__方法来设定
# Mike.sex = u'男'
# print Mike.name, Mike.score, Mike.sex
# print Mike.get_score()


# · 继承，直接传入就完事儿了
# class FreshMan(Student):
#   def happy_every(self):
#     print "I'm happy every day!"
#     return self
#   # 覆盖相同方法
#   def get_score(self):
#     return u'新生学啥习啊？'

# Kitty = FreshMan('Kitty', 59, 18)
# print Kitty.happy_every().get_score()
# print isinstance(Kitty, Student)
# 打印其所有方法and属性
# for property in dir(Kitty):
#   print property

# getattr(), setattr(), hasattr()可直接操作一个对象的状态
# print hasattr(Kitty, 'score')
# print hasattr(Kitty, 'hobby')
# setattr(Kitty, 'hobby', 'CTRL')
# print getattr(Kitty, 'hobby') # 若不存在将会抛出错误AttributeError


## · 类属性（静态属性），所有实例都能访问相同的类属性，甚至不需要实例也能直接通过类名访问
# class Seniors(Student):
#   grade = u'大四'

# Keven = Seniors('Keven', 60, 22)
# print Seniors.grade, Keven.grade

## · __slots__: 给类设置该属性，其值为元组，则将只允许给该类动态添加元组内属性
##   eg: 设置Junior类__slots__ = ('direction', 'wish')，则只能操作这两个属性，其他则会报错
# class Junior(Student):
#   __slots__ = ('name', 'score')
# Kimmy = Junior('Kummy', 98, 21)

## · @property: Python内置的@property装饰器就是负责把一个方法变成属性调用的
##   把一个getter方法变成属性，只需要加上@property就可以了，
##   此时，@property本身又创建了另一个装饰器@score.setter，
##   负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作
class Sophomore(object):
  @property
  def score(self):
    return self._score
  
  @score.setter
  def score(self, value):
    if not isinstance(value, int):
      raise ValueError('score must be an integer')
    if value < 0 or value > 100:
      raise ValueError('score in 0 ~ 100')
    self._score = value
  

  ## 只读属性，即，只定义getter不定义setter
  @property
  def age(self):
    return 18
  

Xiaoming = Sophomore()
# Xiaoming.score = 1000 # Error:
# Xiaoming.age = 19 # Error
Xiaoming.score = 98
# print Xiaoming.age, Xiaoming.score

# · 多重继承：在定义类时，可以追加多个父类，则一个子类能够同时获得多个父类的所有功能
## 如，摩托车，既属于机动车又是两轮车
# class MotorVehicles(object):
#   def refuel(self):
#     print u'加油'

# class TwoWheeler(object):
#   def needBalance(self):
#     print u'需要平衡'

# class MotorBike(MotorVehicles, TwoWheeler):
#   pass

# motorbike = MotorBike()
# motorbike.refuel()
# motorbike.needBalance()
## 注：在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。
## 但是，如果需要“混入”额外的功能，通过多重继承就可以实现，
## 比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。

# · 定制类：
class CMS(object):
  def __init__(self, name):
    self.name = name

  ## 1. __str__: 直接打印类实例文字格式化
  def __str__(self):
    return "Custom-Made-Student: %s" % self.name

  ## 2. __getattr__: 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回一个预设值
  def __getattr__(self, attr):
    if attr == 'score':
      return 99
    else:
      return 'None'

cms1 = CMS('xzxldl55')
print cms1
print cms1.score
print cms1.abb


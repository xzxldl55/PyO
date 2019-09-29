# -*- coding:utf-8 -*-
from enum import Enum

'''
当我们需要定义常量时,可以使用Enum类来定义，其每个属性都是一个常量
'''

Month = Enum('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
print Month.Jan

# 若要进行精确控制枚举类型，可从Enum派生出自定义类

class Weekday(Enum):
  Sun = 0
  Mon = 1
  Tue = 2
  Wed = 3
  Thu = 4
  Fri = 5
  Sat = 6

print Weekday.Sun





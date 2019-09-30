# -*- coding:utf-8 -*-
'''
集合模块
'''

# 1.namedtuple：一个函数，用来创建一个自定义的tuple对象，并且规定了tuple元素个数，可赢属性而非索引来饮用tuple中的某个元素
from collections import Counter
import argparse
import os
from collections import ChainMap
from collections import OrderedDict
from collections import defaultdict
from collections import deque
from collections import namedtuple
# 这样我们可以直接定义一个能够表意的tuple，而不用去新建一个类来表示“点”
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(1, 2)
# print(p1.x, p1.y, p1)
# 类似的我们还能表示圆
Circle = namedtuple('Circle', ['r', 'x', 'y'])
c1 = Circle(1, 0, 0)
# print(c1)

# 2.deque：使用list存储数据时，按索引访问很快，但插入与删除元素很慢（线性存储），而deque则是为了搞笑实现插入与删除操作的双向列表，适用于队列与栈
q = deque(['a', 'b', 'c'])
q.append('x')  # 右插
q.appendleft('y')  # 左插
q.pop()  # 删除尾部
# print(q)

# 3.defaultdict：使用dict时，若果key不存在，则会抛出KeyError错误。如果希望key不存在时返回一个默认值则可使用defaultdict
dd = defaultdict(lambda: 'N/A')  # 接受一个函数作为参数，其返回值为默认值
dd['key1'] = 'abc'
# print(dd['key1'], dd['key2'])

# 4.OrderedDict：有序化的dict，可以保持key的顺序
d = dict([('a', 1), ('b', 2), ('c', 3)])
# print(d)  # 无序的类json对象
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# print(od)

# 5.ChainMap：可以把一组dict串起来拼成一个逻辑上的dict。例如应用程序往往都需要传入参数，参数可以通过命令行传入，可以通过环境变量传入，亦或是默认参数。则能够使用ChainMap实现参数的优先级查找，即先查命令行参数，没有传入再查...

# 如何查找user & color
defaults = {  # 构造默认参数
    'color': 'red',
    'user': 'guest'
}
# 构造命令行参数
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}

# 组合成ChainMap
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数 user=admin color=green python3 collectionsDemo.py -u bob -c white 同时输入了命令行参数与环境变量时
# print('color=%s' % combined['color'])
# print('user=%s' % combined['user'])

# 6.Counter：一个简单的计数器，例如统计字符出现的个数，也是一个dict的子类
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)

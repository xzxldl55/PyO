# -*- coding:utf-8 -*-

import time, sys, queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
  pass
# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器（及master）
server_addr = '127.0.0.1'
print('正在联机服务器 %s' % server_addr)

m = QueueManager(address=(server_addr, 5000), authkey=b'xzxldl55')
m.connect()

# 获取Queue对象
task = m.get_task_queue()
result = m.get_result_queue()

# 从task队列读取任务，并将其结果写入result
for i in range(10):
  try:
    n = task.get(timeout=1)
    print('运行任务 %d * %d' % (n, n))
    r = '%d * %d = %d' % (n, n, n*n)
    time.sleep(1)
    result.put(r)
  except queue.Empty:
    print('任务队列为空')

print('任务处理完毕！')
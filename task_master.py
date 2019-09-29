# -*- coding:utf-8 -*-

# 分布式进程通信 ——> master管理者

import random, time, queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# 发送任务的队列：
task_queue = queue.Queue()
# 接受结果队列
result_queue = queue.Queue()

# 从BaseManger继承QueueManger
class QueueManager(BaseManager):
  pass

## windows不支持register(callable)下调用匿名函数所以封装两个函数
def ret_task():
  global task_queue
  return task_queue
def ret_result():
  global result_queue
  return result_queue

# 将两个Queue都注册到网络上call参数关联Queue对象，使用lambda将queue返回出去
QueueManager.register('get_task_queue', callable=ret_task)
QueueManager.register('get_result_queue', callable=ret_result)
# 将manger绑定到5000端口，并设置验证码用于连接
manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'xzxldl55')



if __name__ == '__main__':
  # 启动manger
  manager.start()
  # 获得通过网络访问到的Queue对象：（由于在同一个文件模块内，所以不需要通过网络访问，直接获得）
  task = manager.get_task_queue()
  result = manager.get_result_queue()
  # 放置几个任务（但不负责运行任务，运行任务交付由另一进程执行）
  for i in range(10):
    n = random.randint(0, 10000)
    print('放置任务 %d' % n)
    task.put(n)
  # 读取result队列
  print('读取结果中...')
  for i in range(10):
    r = result.get(timeout=100)
    print('结果为：%s' % r)
  # 关闭
  manager.shutdown()
  print('master 退出')

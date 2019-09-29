# -*- coding:utf-8 -*-

# 由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。
from multiprocessing import Process, Pool
import os, time, random


'''
process.join()/threading.join()方法是用于使得主进程/主线程与子xx同步的，
因为当默认情况下主xx执行完任务后就退出了，而此时子xx会继续执行自己的任务直到结束。
而使用join后则是将主子同步，当主线程任务结束后，进入阻塞状态，等待其他子xx的结束
最后主xx方才结束。


'''


# 子进程代码
# def run_proc(name):
#   print('Run child process %s.', os.getpid())

# if __name__ == '__main__':
#   print('Parent process %s.', os.getpid())
#   p = Process(target=run_proc, args=('test', ))
#   print('Child process will start.')
#   p.start()
#   p.join()
#   print('Child process end.')

# 使用进程池大量创建子进程
def long_time_task(name):
  print('Run task %s (%s)...' % (name, os.getpid()))
  start = time.time()
  time.sleep(random.random() * 3)
  end = time.time()
  print("Task %s runs %0.2f seconds." % (name, (end - start)))

if __name__ == '__main__':
  print("Parent process %s " % os.getpid())
  p = Pool(4)
  for i in range(5):
    p.apply_async(long_time_task, args=(i, ))
  print(u"Waiting for all 子进程 done...")
  p.close() # close之后便不能再继续添加Process了
  p.join()
  print("All 子进程 done")
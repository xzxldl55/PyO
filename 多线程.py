# -*- coding:utf-8 -*-
import time, threading

'''
多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
'''


# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
# def loop():
#   print(u'线程 %s 正在运行...' % threading.current_thread().name)
#   n = 0
#   while n < 5:
#     n = n + 1
#     print('线程 %s >>> %s' % (threading.current_thread().name, n))
#     time.sleep(1)
#   print('线程 %s 结束。' % threading.current_thread().name)

# print('线程 %s 正在运行...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread') # 创建子线程
# t.start()
# t.join() # 若没有join则主线程在创建完子线程后将直接结束，而子线程将继续执行下去
# print('线程 %s 结束。' % threading.current_thread().name)


# !多线程共享变量而致的混乱：
# balance = 0
def change_it(n):
  # 先加后减，所以balance应该还是0
  global balance
  balance = balance + n
  balance = balance - n

# def run_thread(n): # 每个子线程都重复存取十万遍
#   for i in range(100000):
#     change_it(n)

#   #创建两个子线程并执行
# t1 = threading.Thread(target=run_thread, args=(5, ))
# t2 = threading.Thread(target=run_thread, args=(8, ))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance) # 最终结果不一定为0（t1与t2两线程交替执行，并使用同一变量所导致）

'''
  |||||==> 防止此种现象，则需要给change_it()上一把锁，当某个线程开始执行change_it是，该线程得到锁
          ，因此其他线程无法执行change_it，只能等待锁被释放。如此则不会造成不同线程修改的冲突。
          可以通过threading.Lock()来创建一个锁
  ||=>  锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，
      坏处当然也很多，首先是阻止了多线程并发执行，
      包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。
      其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，
      导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。
'''
# balance = 0
# lock = threading.Lock()

# def run_thread2(n):
#   for i in range(100000):
#     # 获取lock
#     lock.acquire()
#     # 使用try finally确保锁能够被释放
#     try:
#       # 开始操作！！
#       change_it(n)
#     finally:
#       # 释放锁
#       lock.release()

# t1 = threading.Thread(target=run_thread2, args=(5, ))
# t2 = threading.Thread(target=run_thread2, args=(8, ))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)


'''
ThreadLocal: 针对多线程局部变量之前传递不便而出。通过创建全局ThreadLocal，将线程局部变量与之绑定...
'''
# 创建全局ThreadLocal
local_shcool = threading.local()

def process_student():
  # 获取当前线程所关联的stud
  std = local_shcool.student
  print('%s in (%s)' % (std, threading.current_thread().name))

def process_thread(name):
  # 绑定ThreadLocal的stud --> 使用ThreadLocal我们不需要关心哪个线程对应哪个stud，它会帮你找出来
  local_shcool.student = name
  process_student()

t1 = threading.Thread(target=process_thread, args=('Lin', ), name='Lin\'s Thread')
t2 = threading.Thread(target=process_thread, args=('Shelley', ), name='Shelley\'s Thread')
t1.start()
t2.start()
t1.join()
t2.join()
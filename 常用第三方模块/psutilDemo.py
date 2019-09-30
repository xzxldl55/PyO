# -*- coding:utf-8 -*-

'''
在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。
顾名思义，psutil = process and system utilities，它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块。
'''
import psutil
# 1.CUP infomation:
# print(psutil.cpu_count()) # cup逻辑数量
# print(psutil.cpu_count(logical=False)) # cpu物理核心
# print(psutil.cpu_times()) # cpu用户/系统空闲时间
# for x in range(10):
#     print(psutil.cpu_percent(interval=1, percpu=True)) # cup使用率，每秒刷新一次

# 2.Memory information:
# print(psutil.virtual_memory()) # 获取物理内存与交换内存信息，单位Byte
# print(psutil.disk_partitions()) # 磁盘分区情况
# print(psutil.disk_usage('/')) # 磁盘使用情况
# print(psutil.disk_io_counters()) # 磁盘IO

# 3.Network information
# print(psutil.net_io_counters()) # 获取网络读写字节/包的个数
# print(psutil.net_if_addrs()) # 网络接口信息
# print(psutil.net_if_stats()) # 网络接口状态
# for i in psutil.net_connections():
#     print(i, '\n') # 当前网络连接信息 需要sudo 

# 4.Process information:
# print(psutil.pids()) # 所有进程pid
p = psutil.Process(444) # 获取指定pid进程
# print(p.name())  # 进程名称
# print(p.exe())  # 进程exe路径
# print(p.cwd())  # 进程工作目录
# print(p.cmdline())  # 进程启动的命令行
# print(p.ppid())  # 父进程ID
# print(p.parent())  # 父进程
# print(p.children())  # 子进程列表
# print(p.status())  # 进程状态
# print(p.username())  # 进程用户名
# print(p.create_time())  # 进程创建时间
# print(p.terminal())  # 进程终端
# print(p.cpu_times())  # 进程使用的CPU时间
# print(p.memory_info())  # 进程使用的内存
# print(p.open_files())  # 进程打开的文件
# print(p.connections())  # 进程相关网络连接
# print(p.num_threads())  # 进程的线程数量
# print(p.threads())  # 所有线程信息
# print(p.environ())  # 所有线程信息
# print(p.terminate())  # 结束进程

print(psutil.test()) # 类似于ps命令


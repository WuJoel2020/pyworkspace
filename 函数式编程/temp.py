#上方代码用于将以下代码保存为py文件
from multiprocessing import Process
import os
def func():
#     os.getpid()获取当前进程id     os.getppid()获取父进程id
    print('func',os.getpid(), os.getppid())
if __name__ == '__main__':
    print('__main__',os.getpid(), os.getppid())
    p = Process(target=func,)
    p.start()

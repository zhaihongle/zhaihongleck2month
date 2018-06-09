import os
ret = os.fork()


if ret == 0:
    print(ret)
    print("我是子进程%s,我的父进程式%s "%(os.getpid(),os.getppid()))
else:
    print(ret)
    print("我是父进程%s,我的子进程试%s"%(os.getpid(),ret))

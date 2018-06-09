import os
rpid = os.fork()

num = 0

if rpid == 0:
    num+= 1
    print("我是子进程%d"%num)
else:
    num-= 1
    print("我是父进程%d"%num)


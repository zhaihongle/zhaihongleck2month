from multiprocessing import Process
import os

def test(args):
    print("hello i'zijincheng%s"%args)
p = Process(target = test,args=("laowang",))
print("zhixingfujincheng")
p.start()
p.join()
print("zijinchengjieshu")

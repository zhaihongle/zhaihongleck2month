from multiprocessing import Pool
import time
def cook():
    print("妈妈在做饭")
    return "饭好了"
def cook1(args):
    print(args)
p = Pool()
p.apply_async(func=cook,callback=cook1)
while True:
    print("xii")

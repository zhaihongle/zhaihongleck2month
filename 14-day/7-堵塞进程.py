from multiprocessing import Pool
import  os

def worker(i):
    for x in range(3):
        print("执行%d pid = %d"%(i,os.getpid()))
p = Pool(3)
for i in range(5):
    print(i)
    p.apply(worker,(i,))
p.close()
p.join()

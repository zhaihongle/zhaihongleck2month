from threading import Thread,Lock
import time
num = 0
def sing():
    global num
    lock.acquire()
    for i in range(1000):
        num +=1
    print("海草%d"%num)
    lock.release()
def dance():
    global num
    lock.acquire()
    for i in range(100):
        num +=1
    print("跳舞%d"%num)
    lock.release()
lock = Lock()
f = Thread(target = sing)
f.start()
f1 = Thread(target = dance)
f1.start()

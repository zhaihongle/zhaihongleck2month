from threading import Thread
import threading
import time
def sing():
    for i in range(3):
        print("海草")
        time.sleep(1)
def dance():
    time.sleep(1)
    print("跳舞")
f = Thread(target = sing)
f1 = Thread(target = dance)

while True:
    length = len(threading.enumerate())
    print('当前运行的线程数为：%d'%length)
    if length<=1:
        break
    sleep(0.5)
f1.start()
f.start()

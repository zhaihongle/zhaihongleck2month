from threading import Thread
import time
num = 0
def sing():
    global num
    for i in range(1000):
        num +=1
    print("海草%d"%num)
def dance():
    global num
    for i in range(100):
        num +=1
    print("跳舞%d"%num)
f = Thread(target = sing)
f.start()
f1 = Thread(target = dance)
f1.start()

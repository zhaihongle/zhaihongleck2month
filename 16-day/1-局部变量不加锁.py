from threading import Thread

def work():
    num = 1
    num +=2
    print("hello%d"%num)
def work1():
    num  = 1
    num+=1
    print("hello%d"%num)
t = Thread(target = work)
t.start()
t1 = Thread(target = work1)
t1.start()

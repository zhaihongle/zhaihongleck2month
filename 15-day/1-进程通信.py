from multiprocessing import Process,Queue
import time

def write(q):
    for i in ["hello","hi","how do you do"]:
        q.put(i)
        print("put %s to queue"%i)
        time.sleep(2)



def read(q):
    while True:
          if not q.empty():
              value = q.get()
              print ('Get %s from queue.' % value)
              time.sleep(1)
          else:
              break
if __name__ =="__main__":
    q = Queue()
    p1 = Process(target= write,args = (q,))
    p2 = Process(target= read ,args = (q,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    

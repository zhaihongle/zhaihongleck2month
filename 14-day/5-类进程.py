from multiprocessing import Process
class PPPPP(Process):
    def __init__(self):
        Process.__init__(self)
        self.name = "sww"
    def run (self): # run方法滚固定
        for i  in range(5):
            print("mmp")
p =PPPPP()
p.start()
p.join()

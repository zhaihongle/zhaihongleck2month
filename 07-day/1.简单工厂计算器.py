class OP(object):
    def __init__(self,num1 = 0,num2 = 0):
        self.num1 = num1
        self.num2 = num2
    def getResult (self):
        pass
class JIA(OP):
    def getResult(self):
        return self.num1 + self.num2
class JIAN(OP):
    def getResult(self):
        return self.num1 - self.num2
class CHENG(OP):
    def getResult(self):
        return self.num1 * self.num2
class CHU(OP):
    def getResult(self):
        try:
            return self.num1 / self.num2
        except Exception as f:
            print(f)
class FRATORY(object):
    def fratory_op(self,type):
        if type == "+" :
            return JIA()
        if type == "-" :
            return JIAN()
        if type == "*" :
            return CHENG()
        if type == "/" :
            return CHU()


xiao = FRATORY()

x = xiao.fratory_op(input("算法："))
x.num1 =float(input("输入数字"))
x.num2 =float(input("输入数字"))
print(x.getResult())

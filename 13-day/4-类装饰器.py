list = [123,234]
password = 123
class function(object):
    def __init__(self,func):
        print("正在初始化－－－－－")
        self.__func = func
    def __call__(self):
        account = int(input("输入账号"))
        pwd = int(input("输入密码"))
        if account in list and pwd == password:
            self.__func()
        else:
            pass
@function
def test():
    print("我要i")

test()

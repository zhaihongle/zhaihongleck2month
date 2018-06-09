class Dog():
    def __init__(self):
        self.name = "王八蛋"
    @staticmethod
    def xxx():
        print("你是丹丹")
d = Dog ()
print(d.name)
d.xxx()#通过实例对象调用静态方法
Dog.xxx()#通过类对象调用静态方法

class Dog():
    eye = "black"
    def __init__(self):
        self.mao = "yellow"
    def move(self):
        print("跑跑跑")
    @classmethod
    def wark (cls):
        print("汪汪汪")
dog = Dog()
print(dog.eye)
print(dog.mao)
dog.move()
dog.wark()
#类实例可以调用类对象的属性和方法

print(Dog.eye)
#print(Dog.mao)   类对象只能类属性
#Dog.move()       类对象只能调用类方法
Dog.wark()

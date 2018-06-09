class person ():
    def __init__(self):
        self.height = 180
        self.__weight = 666
    def getweight(self):
        return self.__weight
    def __move (self):
        return "跑跑跑" 
    def moves (self):
        return self.__move()
    def __str__(self):
        return "shengao%s"%self.height
    def eat (self):
        print("吃")
class Son (person):
    pass



xiaoming = Son()
xiaoming.eat()
print(xiaoming.getweight())
print(xiaoming)
print(xiaoming.moves())

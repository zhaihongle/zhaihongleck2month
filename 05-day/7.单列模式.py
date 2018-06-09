class Person():
    __istance = None
    __isfalg = False
    def __init__(self,name):
        if self.__isfalg == False:
            self.name = name
            self.__isfalg = True
    def __new__(cls,name):
        if cls. __istance == None:
            cls.__istance = object.__new__(cls)
            print("好好好学习")
            return cls.__istance
        else:
            return cls.__istance
p = Person("ddd")
print(id(p))
p = Person("dsss")
print(id(p))
p = Person("aaaa")
print(id(p))
p = Person("sswww")
print(id(p))
p = Person("qqqqqq")
print(id(p))
p = Person("vvvvv")
print(id(p))
p = Person("ffffff")
print(id(p))
print(p.name)

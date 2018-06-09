def w1(cls):
    istance = {}
    def inner(*args,**kwargs):
        if cls not in istance:
            istance[cls] = cls(*args,**kwargs)
            return istance[cls]
        else:
            return istance[cls]
    return inner

@w1
class Dog(object):
    def __init__(self,x=0):
        self.x = x
dog = Dog()
print(id(dog))
dog1 = Dog()
print(id(dog1))

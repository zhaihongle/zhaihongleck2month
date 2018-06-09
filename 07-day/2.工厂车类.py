class Car(object):
    def __init__(self,color = "褐色",qudong = "八区"):
        self.color = color
        self.qudong = qudong
class Baoma(Car):
    def move (self):
        print("恭喜您购买了宝马")
class Benchi(Car):
    pass
class Lanbor(Car):
    pass
class Laos(Car):
    pass

print("上帝您好：\n奔驰 宝马 兰博基尼 劳斯莱斯\n供您选择")
class BuyCar(object):
    def buycar(self,typename):
        self.name = typename
        if self.name =="宝马":
            return Baoma()   
        elif self.name =="奔驰":
            return Benchi()   
        elif self.name =="兰博基尼":
            return Lanbor()   
        elif self.name =="劳斯莱斯":
            return Laos()   
car = BuyCar()
mycar = car.buycar(input("您要选择的车："))
mycar.move()

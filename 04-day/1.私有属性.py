class person():
    def __init__(self):
        self.__money = 200
    def getMoney(self):
        return self.__money
    def setMoney (self,money):
        if money > 0 :
            self.__money = money
        else:
            print("输入有误")
xiaoming = person()
xiaoming.setMoney(-300)
print(xiaoming.getMoney())


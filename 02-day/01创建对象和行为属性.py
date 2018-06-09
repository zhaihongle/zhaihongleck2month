class Pig():
    def sleep(self):
        print("%s在睡觉"%self.name)
    def eat (self):
        print("%s吃饲料"%self.name)
    def introuduce(self):
        print("名字%s\n年龄%s\n颜色%s"%(self.name,self.age,self.color))

peiqi = Pig()
peiqi.name = input("请输入名字")
peiqi.age = 12
peiqi.color = "粉色"
peiqi.sleep()
peiqi.eat()
peiqi.introuduce()


qz = Pig()
qz.name = "乔治"
qz.age =8 
qz.color = "蓝色"
qz.sleep()
qz.eat()
qz.introuduce()

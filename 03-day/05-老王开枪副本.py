class Person ():
    def __init__(self,name):
        self.name = name
        self.hp = 100
        self.gun = None
    def addgun (self):
        self.gun = gun
    def __str__(self):
        return "名字：%s\nHP:%s\n武器：%s"%(self.name,self.hp,gun.name)
    def zhuangzidan(self,danjia,zidan):
        danjia.addzidan(zidan)
    def zhuangdanjia(self,gun,danjia):
        gun.adddanjia(danjia)
    def opengun (self,diren):
        if diren.hp>0:
            zidans = self.gun.popgunzidan()
            if zidans:
                zidans.kill(diren)
            else:
                print("没子弹")
class Gun ():
    def __init__(self,name):
        self.name = name 
        self.danjia = None
    def adddanjia(self,danjia):
        self.dnajia = danjia
    def popgunzidan(self):
        return danjia.popzidan()
class Danjia():
    def __init__(self):
        self.zidan_list = []
    def addzidan(self,zidan):
        self.zidan_list.append(zidan)
    def popzidan(self):
        if self.zidan_list:
            return self.zidan_list.pop()
        else:
            return None

class Zidan():
    def __init__(self,weili):
       self.weili = weili
    def kill (self,diren):
        diren.hp-=self.weili
        if diren.hp >0:
            print("%s剩余%s血"%(diren.name,diren.hp))
        else:
            print("%s死了"%diren.name)



laowang = Person("老王")
gun = Gun("98k")
print(laowang)
danjia = Danjia()
laowang.addgun()
for i in range(30):
    zidan = Zidan(30)
    laowang.zhuangzidan(danjia,zidan)
laowang.zhuangdanjia(gun,danjia)
diren = Person("老宋")
laowang.opengun(diren)
laowang.opengun(diren)
laowang.opengun(diren)
laowang.opengun(diren)
laowang.opengun(diren)

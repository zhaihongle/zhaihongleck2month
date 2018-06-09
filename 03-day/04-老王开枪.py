class people():
    def __init__(self,name):
        self.name = name
        self.hp = 100
        self.gun = None
    def zhuangzidan(self,danjia,bullet):
        danjia.addBullet(bullet)
    def zhuangdanjia(self,gun,danjia):
        gun.addDanjia(danjia)
    def takeGun(self,gun):
        self.gun = gun
    def openGun(self,diren):
        if diren.hp>0:
            zidan = self.gun.popGunBullet()
            if zidan:
                zidan.kill(diren)
            else:
                print("没子弹")

class Gun():
    def __init__(self,name,):
        self.name = name
        self.danjia = None
       
    def addDanjia(self,danjai):
        self.danjia= danjia
    def popGunBullet(self):
        return self.danjia.popBullet()
class Danjia():
    def __init__(self,size):
        self.size = size
        self.bullet_list =[]
    def addBullet(self,bullet):
        self.bullet_list.append(bullet)
    def popBullet(self):
        if self.bullet_list:
            return self.bullet_list.pop()
        else:
            return None
class Bullet():
    def __init__(self):
        self.weli = 20
    def kill (self,diren):
        diren.hp -=self.weli
        if diren.hp <=0:
            diren.hp = 0
            print("%s死了，剩余血量%s"%(diren.name,diren.hp))
        else:
            print("%s剩余血量%s"%(diren.name,diren.hp))

p = people("老王")
qiang = Gun("98K")
danjia = Danjia(30)
for i in range(30):
    bullet = Bullet()
    p.zhuangzidan(danjia,bullet)    
p.zhuangdanjia(qiang,danjia)

p1 = people("老宋")
p.takeGun(qiang)
p.openGun(p1)
p.openGun(p1)
p.openGun(p1)
p.openGun(p1)
p.openGun(p1)
p.openGun(p1)
p.openGun(p1)
p.openGun(p1)
p.openGun(p1)





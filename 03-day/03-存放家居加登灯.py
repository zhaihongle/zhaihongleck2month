class Home():
    def __init__(self,area,hometype,address):
        self.area = area
        self.hometype = hometype
        self.address = address
        self.jiaju = []
        self.s_light = []
    def __str__(self):
        msg = "房子是%s平\n房子有%s\n房子在%s"%(self.area,self.hometype,self.address)
        return msg
    def addBed(self):
        if self.area >= mybed.bedtype:
            self.jiaju.append(mybed)
            self.area-=mybed.bedtype
            print("加入成功")
        else:
            print("加入失败")
    def addlight(self,light):
        self.s_light.append(light)
    def switch(self):
        if self.s_light[0].getIsopen():
            self.s_light[0].close()
        else:
            self.s_light[0].open()
class Bed():
    def __init__(self,bedtype,name):
        self.bedtype = bedtype
        self.name = name
    def __str__(self):
        return "床的大小是%d\n床的品牌是%s"%(self.bedtype,self.name)
class Light():
    def __init__(self,name):
        self.name = name
        self.Isopen = False
    def __str__(self):
        return "灯的品牌是%s"%self.name
    def open (self):
        print("灯亮了")
        self.Isopen =True
    def close(self):
        print("灯灭了")
        self.Isopen = False
    def getIsopen (self):
        return self.Isopen
     
myhome = Home(120,"三室一厅","北京长安街６６６号")
print(myhome)
mybed = Bed(40,"席梦思")
print(mybed)
light = Light("阿拉丁")
print(light)

myhome.addBed()
myhome.addBed()
myhome.addBed()
myhome.addBed()
myhome.addBed()
myhome.addBed()
myhome.addBed()
myhome.addlight(light)
for i in range(8):
    myhome.switch()

class Home():
    def __init__(self,area,hometype,address):
        self.area = area
        self.hometype = hometype
        self.address = address
        self.jiaju = []
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
class Bed():
    def __init__(self,bedtype,name):
        self.bedtype = bedtype
        self.name = name
    def __str__(self):
        return "床的大小是%d\n床的品牌是%s"%(self.bedtype,self.name)

     
myhome = Home(120,"三室一厅","北京长安街６６６号")
print(myhome)
mybed = Bed(40,"席梦思")
print(mybed)


myhome.addBed()
myhome.addBed()
myhome.addBed()
myhome.addBed()
myhome.addBed()
myhome.addBed()
myhome.addBed()

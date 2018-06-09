
c=0
while True:
    c+=1
    class hulu():
        def dayaoguai(self):
            print("%s打蛇精"%self.name)
        def baohu(self):
            print("%s保护爷爷"%self.name)
        def introduce(self):
            print("头发%s\n衣服%s\n超能力%s\n"%(self.hear,self.yifu,self.chao))
    one = hulu()
    one.name = input('名字')
    one.hear = input("头发")
    one.yifu = input("衣服")
    one.chao = input("超能力")
    one.dayaoguai()
    one.baohu()
    one.introduce()
    if c == 3:
        break


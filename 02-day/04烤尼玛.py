class NiMa():
    def __init__(self):
        self.time =0 #烤尼玛的时间
        self.end = '生的'    #烤尼玛的程度
        self.list = []
    def s_time(self,time,sss):
        self.time+=time
        if self.time > 0 and self.time < 5:
            self.end = "半生不熟"
            self.list.append(sss)
        elif self.time >= 5 and self.time < 7:
            self.end = "八成熟"
            self.list.append(sss)
        elif self.time >=7 and self.time < 10:
            self.end = "熟透了"
            self.list.append(sss)
    def __str__(self):
        return "尼玛现在%s加了%s"%(self.end,self.list)
nima = NiMa()
nima.s_time(2,"辣椒")
print(nima)
nima.s_time(2,"芥末")
print(nima)
nima.s_time(2,"大蒜")
print(nima)
nima.s_time(1,"大葱")
print(nima)
nima.s_time(1,"大酱")
print(nima)
nima.s_time(1,"臭豆腐")
print(nima)

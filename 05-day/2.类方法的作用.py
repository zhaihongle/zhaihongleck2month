class Date():
    def __init__(self,year,month,day):
        self.year = year
        self.month = month 
        self.day = day
    def outdate (self):
        print("%s年%s月%s日"%(self.year,self.month,self.day))
    @classmethod
    def youhuadate(cls,date):
        a,b,c = date.split("-")
        return cls(a,b,c) 
        # d = cls(a,b,c)       
        # return d



date = "2018-05-06"
Date.youhuadate(date).outdate()
#d = youhuadate()
#d.outdate










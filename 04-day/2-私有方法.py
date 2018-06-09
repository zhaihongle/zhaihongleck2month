class Money():
    def __money(self,money):
        self.money =100
        self.money-=money
        print("扣钱，发短信") 
    def publicmoney(self,money):
        if money > 0 :
            self.__money(money)
        else:
            print("发送失败")
mm = Money()
mm.publicmoney(11)

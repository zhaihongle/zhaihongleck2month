class BOY():
    def __init__(self,age,height):
        self.age =age
        self.height =height
        self.game = []
    def sleep(self,time):
        print('sleep%shour'%time)
    def eat(self):
        print('eat ')
    def showage(self):
        print('%s'%self.age)
    def showgame(self):
        for i in range(3):
            games = input('请输入游戏名字')    
            self.game.append(games)
        print(self.game)
zhl = BOY(12,34)
zhl.sleep(18)
zhl.eat()
zhl.showage()
zhl.showgame()

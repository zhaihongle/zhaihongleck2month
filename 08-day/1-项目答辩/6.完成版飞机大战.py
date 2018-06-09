#coding = utf-8
import pygame 
from plane_sprites import *
HERO_FIRE_EVENT = pygame.USEREVENT +1
pygame.init()
strt=u"得分"
font = pygame.font.Font("./images/NotoSansCJK-Black.ttc", 40)
text = font.render(strt,True,(0,0,200))

class PlanGame(object):
    #初始化
    def __init__(self):
        print("游戏初始化")
        #创建窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #创建时钟对象
        self.clock = pygame.time.Clock()
        self.__create_sprite()

        pygame.time.set_timer( CREATE_ENEMY_EVENT,1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,500)
        self.enemy_group = pygame.sprite.Group()
        #敌机销毁精灵组
        self.enemy1_down_group = pygame.sprite.Group()
        self.count = 0
        self.score = 0 #分数

    #开始游戏
    def startGame(self):
        print("开始游戏")   
        while True:
            self.clock.tick(80)
            self.__event_handler()
            self.__check_collide()
            self.screen.blit(text,(320,20))
            pygame.display.update()
            self.__update_sprites()
            


    #创建精灵或精灵组
    def __create_sprite(self):
        bg = background()
        bg1 = background(True)
        self.back_group = pygame.sprite.Group(bg,bg1)
        
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    #事件监听
    def __event_handler(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 8
            self.hero.speed1 = 0
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -8
            self.hero.speed1 = 0
        elif keys_pressed[pygame.K_UP]:
            self.hero.speed1 = -8
            self.hero.speed = 0
        elif keys_pressed[pygame.K_DOWN]:
            self.hero.speed1 = 8
            self.hero.speed = 0
        else:
            self.hero.speed1 = 0
            self.hero.speed = 0
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlanGame.__game_over(self)
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

    #碰撞检测
    def __check_collide(self):
        enemy_down = pygame.sprite.groupcollide(self.enemy_group,self.hero.bullets, True, True)
        enemy1_down_group.add(enemy_down)
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            self.hero.kill()
            PlanGame.__game_over(self)
    #更新精灵组
    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)
        
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)
        self.drawText(str(self.score),SCREEN_RECT.width - 30,50)
		#敌机销毁
        for enemy1_down in enemy1_down_group:
            self.screen.blit(enemy1_down_surface[enemy1_down.down_index],enemy1_down.rect)
            if self.count % 5 == 0:
                enemy1_down.down_index += 1
                if enemy1_down.down_index == 3:
                    self.score += 2
                    enemy1_down_group.remove(enemy1_down)
                    print(self.score)
    def __game_over(self):
        print("游戏结束")   
        pygame.quit()
        exit() 
    def drawText(self,text,posx,posy,textHeight=48,fontColor=(0,0,200),backgroudColor=(255,255,255)):
        fontObj = pygame.font.Font(None, textHeight)  # 通过字体文件获得字体对象
        textSurfaceObj = fontObj.render(text, True,fontColor,backgroudColor)  # 配置要显示的文字
        textRectObj = textSurfaceObj.get_rect()  # 获得要显示的对象的rect
        textRectObj.center = (posx, posy)  # 设置显示对象的坐标
        self.screen.blit(textSurfaceObj, textRectObj)  # 绘制字	 

if __name__ == '__main__':
    plangame = PlanGame()
    plangame.startGame()

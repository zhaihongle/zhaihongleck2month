import random 
import pygame
CREATE_ENEMY_EVENT =pygame.USEREVENT

#HERO_FIRE_EVENT = pygame.USEREVENT +1
FEAM_PER_SEC = 60
SCREEN_RECT = pygame.Rect(0,0,480,750)
#子弹事件常量
CREATE_BULLET_EVENT = pygame.USEREVENT + 1

#爆炸销毁图片
bg1 = pygame.image.load('./images/enemy1_down1.png')
bg2 = pygame.image.load('./images/enemy1_down2.png')
bg3 = pygame.image.load('./images/enemy1_down3.png')
bg4= pygame.image.load('./images/enemy1_down4.png')

#爆炸的精灵组
enemy1_down_group = pygame.sprite.Group()

#把爆炸图片放到列表中
enemy1_down_surface = []
enemy1_down_surface.append(bg1)
enemy1_down_surface.append(bg2)
enemy1_down_surface.append(bg3)
enemy1_down_surface.append(bg4)

class GameSprite(pygame.sprite.Sprite):
    def  __init__(self,image_name,speed = 1,speend = 1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
    def update(self):
        self.rect.y += self.speed
class background(GameSprite):
    def __init__(self,is_alt=False):
        self.image_name = "./images/background.png"
        super().__init__(self.image_name)
        if is_alt:
            self.rect.y -= self.rect.height
    def update (self):
        super().update()
        self.rect.y += self.speed
        if self.rect.y >= SCREEN_RECT.height:
             self.rect.y = -self.rect.height
class Enemy (GameSprite):
    def __init__(self):
        self.image_name = "./images/enemy1.png"
        super().__init__(self.image_name)
        
        self.speed = random.randint(1,5)
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)
        self.down_index = 0
        
    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()
class Hero(GameSprite):
    def __init__(self):
        super().__init__("./images/hero1.png",0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom-100
        self.bullets  = pygame.sprite.Group()
        self.speed1 = 0
    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed1
        if self.rect.left <0:
            self.rect.left = 0
        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        if self.rect.y <0:
            self.rect.y = 0
        if self.rect.bottom > SCREEN_RECT.height:
            self.rect.bottom = SCREEN_RECT.height
    def updateud(self):
        self.rect.y += self.speend
    def fire (self):
        for i in (1,2,3):
            bullet = Bullet()
            if i == 1:
                bullet.rect.x = self.rect.centerx
                bullet.rect.y = self.rect.y - 10
            elif i ==2:
                bullet.rect.x = self.rect.centerx - 40
                bullet.rect.y = self.rect.y - 10
            elif i ==3:
                bullet.rect.x = self.rect.centerx + 40
                bullet.rect.y= self.rect.y - 10
            self.bullets.add(bullet)

class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet2.png",-2)
    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()




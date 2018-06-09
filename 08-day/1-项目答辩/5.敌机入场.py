import pygame
from plane_sprites import *
pygame.init()
screen = pygame.display.set_mode((480,720))
bg = pygame.image.load("./images/background.png")
#screen.blit(bg,(0,0))

hero = pygame.image.load("./images/hero1.png")
screen.blit(hero,(180,500))

clock = pygame.time.Clock() #创建时钟

hero_ret = pygame.Rect(180,500,200,200) #创建英雄的坐标和宽度长度
enemy1 = GameSprite("./images/enemy1.png")
enemy2 = GameSprite("./images/enemy1.png")
enemy2.rect.x = 200
enemy_group = pygame.sprite.Group(enemy1,enemy2)
while True:
    clock.tick(60)
    if hero_ret.y > 0:
        
        hero_ret.y -= 8
        screen.blit(bg,(0,0))#覆盖背景
        screen.blit(hero,hero_ret)
    elif hero_ret.y <= 0:
        hero_ret.y = 700

    enemy_group.update()
    enemy_group.draw(screen)
    pygame.display.update()

    #监听退出
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

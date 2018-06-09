import pygame
pygame.init()
screen = pygame.display.set_mode((480,720))
bg = pygame.image.load("./images/background.png")
#screen.blit(bg,(0,0))

hero = pygame.image.load("./images/hero1.png")
screen.blit(hero,(180,500))

clock = pygame.time.Clock() #创建时钟

hero_ret = pygame.Rect(180,500,200,200) #创建英雄的坐标和宽度长度

while True:
    clock.tick(60)
    if hero_ret.y > 0:
        hero_ret.y -= 8
        screen.blit(bg,(0,0))#覆盖背景
        screen.blit(hero,hero_ret)
        pygame.display.update()
    elif hero_ret.y +hero_ret.height <= 0:
        hero_ret = pygame.Rect(180,500,200,200) #创建英雄的坐标和宽度长度
        pygame.display.update()
    #监听退出
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

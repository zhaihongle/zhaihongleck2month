import pygame
pygame.init()
screen = pygame.display.set_mode((480,720))
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))
hero = pygame.image.load("./images/hero1.png")
screen.blit(hero,(200,500))
pygame.display.update()

while True:
    pass
pygame.quit()

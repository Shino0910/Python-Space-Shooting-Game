from ast import While
from turtle import width
import pygame

White=(105,105,105)
Width = 500
Heigh = 600

# inintilize the game & create window
pygame.init()
screen = pygame.display.set_mode((Width, Heigh))
pygame.display.set_caption("Space Shooting Game")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill((0 ,255, 0))
        self.rect = self.image.get_rect()



# loop
# update the game


running =True
while running:
    clock.tick(60)
    # access the input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
    
    # display
    screen.fill(White)
    pygame.display.update()
pygame.quit()           
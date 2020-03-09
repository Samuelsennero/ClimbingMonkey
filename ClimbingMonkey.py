import pygame
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (102, 51, 0)
LIGHTBLUE = (153, 179, 255)
 
pygame.init()

size = (400, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Climbing Monkey")


#Trees

treesImg = pygame.image.load('mvp_trees.png')

def trees(x):
    screen.blit(treesImg, (0, x))
    screen.blit(treesImg, (0, x - 600))
 
#Monkey

monkeyImg = pygame.image.load('monkey_mvp.png')
monkeyflipImg = pygame.image.load('monkey_mvp_flip.png')

def monkey(x):
    if x < 200:
      screen.blit(monkeyImg, (x, 300))
    else:
        screen.blit(monkeyflipImg, (x, 300))

done = False
 
clock = pygame.time.Clock()

y = 0
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    

    screen.fill(LIGHTBLUE)

    new_tree = y % treesImg.get_rect().height
    screen.blit(treesImg, (0, new_tree - treesImg.get_rect().height))
    if new_tree < 600:
        screen.blit(treesImg, (0, new_tree))
        
    y += 3
 

    


   

    monkey(60)




    pygame.display.flip()




    clock.tick(60)
 

pygame.quit()
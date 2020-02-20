import pygame
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (102, 51, 0)
 
pygame.init()

size = (400, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Climbing Monkey")


#Trees

treesImg = pygame.image.load('mvp_trees.png')

def trees(x):
    screen.blit(treesImg, (0, x))
 

 
done = False
 
clock = pygame.time.Clock()
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
 


    screen.fill(GREEN)

    for i in range(600):
        trees(i)
 

    pygame.display.flip()
 

    clock.tick(60)
 

pygame.quit()

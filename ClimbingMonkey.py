import pygame
import time
import random

#Color definitions
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (102, 51, 0)
LIGHTBLUE = (153, 179, 255)

#Screen setup
pygame.init()

size = (400, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Climbing Monkey")

#Branch sprites
branchImg = pygame.image.load('branch_mvp.png')
branchflipImg = pygame.image.load('rotated_branch_mvp.png')


#Tree sprites
treeImg = pygame.image.load('mvp_trees.png')
 
#Monkey sprites
monkeyImg = pygame.image.load('monkey_mvp.png')
monkeyflipImg = pygame.image.load('monkey_mvp_flip.png')

monkey_x = 60
monkey_y = 300
flipped = False

monkeyflip = monkeyImg
    
#Variables

done = False
 
clock = pygame.time.Clock()

y = 0
 
#Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if flipped == False:
                    monkeyflip = monkeyflipImg
                    monkey_x += 160
                    flipped = True
                elif flipped == True:
                    monkeyflip = monkeyImg
                    monkey_x -= 160
                    flipped = False

                
 
    #Animations
    screen.fill(LIGHTBLUE)

    chance = random.randint(0, 300)
    chanceflip = random.randint(0, 1)
    

    new_tree = y % treeImg.get_rect().height
    screen.blit(treeImg, (0, new_tree - treeImg.get_rect().height))
    if new_tree < 600:
        screen.blit(treeImg, (0, new_tree))
    if new_tree == chance and chanceflip == 0:
        screen.blit(branchImg, (60, 300))
    elif new_tree == chance and chanceflip == 1:
        screen.blit(branchflipImg, (220, 300))
        
        
    y += 3

    screen.blit(monkeyflip,(monkey_x,monkey_y))
    
 


    pygame.display.flip()




    clock.tick(60)
 

pygame.quit()
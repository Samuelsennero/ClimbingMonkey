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
LIGHT = (254, 251, 232)

#Screen setup
pygame.init()
 
size = (400, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Climbing Monkey")

#Menu screen
menuImg = pygame.image.load('Images/programmering_loadingscreen.jpg')

#How to play
howtoplayImg = pygame.image.load('Images/how_to_play.png')
 
#Branch sprites
branchImg = pygame.image.load('Images/branch_mvp.png')
branchflipImg = pygame.image.load('Images/rotated_branch_mvp.png')

#Tree sprites
treeImg = pygame.image.load('Images/mvp_trees.png')
 
#Monkey sprites
monkeyImg = pygame.image.load('Images/monkey_mvp.png')
monkeyflipImg = pygame.image.load('Images/monkey_mvp_flip.png')

monkey_x = 60
monkey_y = 300
flipped = False

monkeyflip = monkeyImg

    
#Variables
spawnbranch = False
spawnflippedbranch = False

branchpos = 0
flippedbranchpos = 0

menu = True

done = False
 
clock = pygame.time.Clock()

menuscreen = menuImg

y = 0

b = 0

f = 0

 #Music
pygame.mixer.music.load('Music/Our-Mountain_v003.mp3')
pygame.mixer.music.play(-1)

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
                    

              
    while menu == True:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                done = True
                menu = False
        if event.type == pygame.MOUSEBUTTONDOWN:
             if event.button == 1:
                    mousepos = pygame.mouse.get_pos()
             if 380 >= mousepos[0] >= 250 and 400 >= mousepos[1] >= 330 and menuscreen == menuImg:
                    menu = False    
             elif 130 >= mousepos[0] >= 0 and 370 >= mousepos[1] >= 315:
                    menuscreen = howtoplayImg
             elif 385 >= mousepos[0] >= 260 and 405 >= mousepos[1] >= 345 and menuscreen == howtoplayImg:
                    menuscreen = menuImg
     screen.blit(menuscreen, (0, 0))
     pygame.display.flip()
     clock.tick(15)
    
    #Animations and spawns
    screen.fill(LIGHTBLUE)
    

    #Branch randomizer
    if spawnbranch == False and spawnflippedbranch == False:
       chance = random.randrange(0, 90, 3)
       chanceflip = random.randint(0, 1)

    #Tree animation
    new_tree = y % treeImg.get_rect().height
    screen.blit(treeImg, (0, new_tree - treeImg.get_rect().height))
    if new_tree < 600:
        screen.blit(treeImg, (0, new_tree))
    
    #Branch spawning
    if new_tree == chance and chanceflip == 0 and spawnbranch == False:
        spawnbranch = True
    elif new_tree == chance and chanceflip == 1 and spawnflippedbranch == False:
        spawnflippedbranch = True
    
    if branchpos == 200:
        spawnbranch = False
    if flippedbranchpos == 200:
        spawnflippedbranch = False

    if spawnbranch == True:
        new_branch = b % treeImg.get_rect().height
        screen.blit(branchImg, (60, new_branch - branchImg.get_rect().height))
        branchpos += 1
        b += 3
    elif spawnflippedbranch == True:
        new_flippedbranch = f % treeImg.get_rect().height
        screen.blit(branchflipImg, (220, new_flippedbranch - branchflipImg.get_rect().height))
        flippedbranchpos += 1
        f += 3
    elif branchpos == 200:
        branchpos = 0
    elif flippedbranchpos == 200:
        flippedbranchpos = 0

    #Branch collision
    if monkey_y + 100 > branchpos * 3 - 126 > monkey_y and flipped == False:
        menu = True
        monkeyflip = monkeyflipImg
        monkey_x += 160
        flipped = True
       
    if monkey_y + 100 > flippedbranchpos * 3 - 126 > monkey_y and flipped == True:
        menu = True
        monkeyflip = monkeyImg
        monkey_x -= 160
        flipped = False
    
    #Game speed
    y += 3

    screen.blit(monkeyflip,(monkey_x,monkey_y))


    pygame.display.flip()




    clock.tick(60)
 

pygame.quit()
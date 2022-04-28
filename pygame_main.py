import pygame
import sys
import os
from player import Player
from helper import random_recipe, time_left, draw_timer, draw_money,draw_recipe
'''
Variables
'''
worldx = 960
worldy = 720
fps   = 40  # frame rate
ani   = 4   # animation cycles
BLUE  = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 0, 0)
main = True
money = 0
ingredients = ["Strawberry","Canteloup","Grape"]


'''
Setup
'''
pygame.init()
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)

world = pygame.display.set_mode([worldx,worldy])
backdrop = pygame.image.load(os.path.join('images','stage.png'))
backdropbox = world.get_rect()

player = Player()   # spawn player
player.rect.x = 0   # go to x
player.rect.y = 275   # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10  # how many pixels to move

start_time = pygame.time.get_ticks()
recipes = random_recipe(20)
counter = time_left()

'''
Main loop
'''
    
while main:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT: 
            counter -= 1
            print(counter)
            text = str(counter).rjust(3) if counter > 0 else 'boom!'
        if counter < 0: 
            pygame.quit()
            sys.exit()
            main = False 


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0,-steps)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, steps)
            
            if event.key == ord('f'):
                if 50 < player.rect.x < 250 and player.rect.y > 500:
                    player.isplate = True
                    player.pick_up(1)

                if player.isplate:
                    if 50 < player.rect.x < 250 and player.rect.y < 315:
                        if player.plate[0] == False:
                            player.plate[0] = True
                            if player.plate[1] == False and player.plate[2] == False:
                                player.pick_up(2)
                            elif player.plate[1] == True and player.plate[2] == False:
                                player.pick_up(5)
                            elif player.plate[1] == True and player.plate[2] == True:
                                player.pick_up(6)
                            else:
                                player.pick_up(8)

                    elif 355 < player.rect.x < 600 and player.rect.y < 315:
                        if player.plate[1] == False:
                            player.plate[1] = True
                            if player.plate[0] == False and player.plate[2] == False:
                                player.pick_up(3)
                            elif player.plate[0] == True and player.plate[2] == False:
                                player.pick_up(5)
                            elif player.plate[0] == False and player.plate[2] == True:
                                player.pick_up(7)
                            else:
                                player.pick_up(8)  

                    elif 655 < player.rect.x < 910 and player.rect.y < 315:
                        if player.plate[2] == False:
                            player.plate[2] = True
                            if player.plate[0] == False and player.plate[1] == False:
                                player.pick_up(4)
                            elif player.plate[0] == True and player.plate[1] == False:
                                player.pick_up(6)
                            elif player.plate[0] == False and player.plate[1] == True:
                                player.pick_up(7)
                            else:
                                player.pick_up(8)
                    else:
                        pass
                else: 
                    print("you need a plate")

            if event.key == ord('e'):
                if 760 < player.rect.x < 910 and player.rect.y > 500:
                    player.toss()

                elif 355 < player.rect.x < 655 and player.rect.y > 500:
                    player.sell(recipes)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, steps)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, -steps)
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False 


        # defining boundary 
        if player.rect.x < 0:
            player.rect.x = 0
        elif player.rect.x > 900:
            player.rect.x = 900
        elif player.rect.y < 275:
            player.rect.y = 275
        elif player.rect.y > 536:
            player.rect.y = 536


    world.blit(backdrop, backdropbox)
    draw_timer(world, 860, 55, time_left())
    draw_money(world, 700, 55, player.geld)
    draw_recipe(world, 30, 55, recipes[player.recipe_counter])
    player.update()  # update player position
    player_list.draw(world) # draw player
    pygame.display.flip()
    clock.tick(fps)
    

"""
MAIN play file for Overcooked
"""
import sys
import os
import pygame
from player import Player
from helper import (draw_small_timer, random_recipe, time_left, draw_timer, draw_money,
draw_recipe, PopUp)

# Variable

WORLDX = 960
WORLDY = 720
FPS = 40  # frame rate
ANI = 4   # animation cycles
BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 0, 0)
MAIN = True
ingredients = ["Strawberry", "Canteloupe", "Grape"]


'''
Setup
'''
pygame.init()
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)

world = pygame.display.set_mode([WORLDX, WORLDY])
backdrop = pygame.image.load(os.path.join('images', 'stage.png'))
backdropbox = world.get_rect()

player = Player()   # spawn player
player.rect.x = 0   # go to x
player.rect.y = 275   # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
STEP = 10  # how many pixels to move

pop_ups = PopUp()
pop_ups.rect.x = 280   # go to x
pop_ups.rect.y = 360   # go to y
pop_ups_list = pygame.sprite.Group()
pop_ups_list.add(pop_ups)

start_time = pygame.time.get_ticks()
recipes = random_recipe(20)
counter = time_left()
timer_list = []

'''
MAIN loop
'''

while MAIN:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            counter -= 1
            #text = str(counter).rjust(3) if counter > 0 else '0'

        if counter >= 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    player.control(-STEP, 0)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    player.control(STEP, 0)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    player.control(0, -STEP)
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    player.control(0, STEP)

                if event.key == ord('f'):
                    if 50 < player.rect.x < 250 and player.rect.y > 500:
                        player.isplate = True
                        player.pick_up(1)

                    if player.isplate:
                        if 50 < player.rect.x < 250 and player.rect.y < 315:
                            if player.plate[0] is False:
                                player.plate[0] = True
                                if (player.plate[1] is False and
                                player.plate[2] is False):
                                    player.pick_up(2)
                                elif (player.plate[1] is True and
                                player.plate[2] is False):
                                    player.pick_up(5)
                                elif (player.plate[1] is True and
                                player.plate[2] is True):
                                    player.pick_up(6)
                                else:
                                    player.pick_up(8)

                        elif 355 < player.rect.x < 600 and player.rect.y < 315:
                            if player.plate[1] is False:
                                player.plate[1] = True
                                if (player.plate[0] is False and
                                player.plate[2] is False):
                                    player.pick_up(3)
                                elif (player.plate[0] is True and
                                player.plate[2] is False):
                                    player.pick_up(5)
                                elif (player.plate[0] is False and
                                player.plate[2] is True):
                                    player.pick_up(7)
                                else:
                                    player.pick_up(8)

                        elif 655 < player.rect.x < 910 and player.rect.y < 315:
                            if player.plate[2] is False:
                                player.plate[2] = True
                                if (player.plate[0] is False and
                                player.plate[1] is False):
                                    player.pick_up(4)
                                elif (player.plate[0] is True and
                                player.plate[1] is False):
                                    player.pick_up(6)
                                elif (player.plate[0] is False and
                                player.plate[1] is True):
                                    player.pick_up(7)
                                else:
                                    player.pick_up(8)

                        elif 655 < player.rect.x < 910 and 350 < player.rect.y < 450:
                            if player.plate[2] is True and player.raisin is False:
                                timer_list.append(pygame.time.get_ticks())
                                print(timer_list)
                                player.raisin = True
                                # change the player icon into cooking
                                #while player.raisin == True:
                                # oh sh*t I don't know how to visualize the timer
                                # let's make the game harder by making timer invisible
                                # the player has to guess how much time has passed
                                # the cooking time must be within 3-5 s
                                # world.blit(backdrop, backdropbox)
                                draw_small_timer(world, 860, 55, 1)
                                


                                

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
                    player.control(STEP, 0)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    player.control(-STEP, 0)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    player.control(0, STEP)
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    player.control(0, -STEP)

                if 655 < player.rect.x < 910 and 350 < player.rect.y < 450:
                    if event.key == ord('f'):
                        timer_list.append(pygame.time.get_ticks())
                        if not 3000 <= timer_list[1] - timer_list[0] <= 5000:  
                                    player.plate[2] = False
                                    player.raisin = False
                                    player.geld -= 10
                        else:
                                    #print(pygame.time.get_ticks())
                                    #timer_list = []
                                    #player.plate[2] = False
                            player.plate[2] = False
                            print(timer_list)
                            print(player.plate)
                            print(player.raisin)


        if event.type == pygame.KEYUP:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                MAIN = False

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
    if counter >= 0:
        draw_timer(world, 860, 55, time_left())
        draw_money(world, 700, 55, player.geld)
        draw_recipe(world, 30, 55, recipes[player.recipe_counter])
    else:
        pygame.sprite.Sprite.kill(player)
        # pop_ups.change(1)
        pop_ups_list.draw(world)
        draw_money(world, 540, 450, f"{player.geld}")

    player.update()  # update player position
    player_list.draw(world)  # draw player
    pygame.display.flip()
    clock.tick(FPS)

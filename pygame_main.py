"""
MAIN play file for Overcooked
"""
import sys
import os
import pygame
from player import Player
from helper import (draw_small_timer, random_recipe, time_left, draw_timer, draw_money,
draw_recipe, PopUp, Stove)

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
ingredients = ["Strawberry", "Canteloupe", "Grape","Raisin"]


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

stove = Stove()
#stove.rect.x = 835   # go to x
stove.rect.x = 280
stove.rect.y = 342   # go to y
stove_list = pygame.sprite.Group()
stove_list.add(stove)
stove_list.draw(world)

start_time = pygame.time.get_ticks()
recipes = random_recipe(20)
counter = time_left()
timer_list = []
stove = False

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

                        elif 355 < player.rect.x < 600 and player.rect.y < 315:
                            if player.plate[1] is False:
                                player.plate[1] = True

                        elif 655 < player.rect.x < 910 and player.rect.y < 315:
                            if player.plate[2] is False:
                                player.plate[2] = True

                    else:
                        print("you need a plate")

                if player.isplate == True:
                    if player.plate == [True, False, False,False]:
                        player.pick_up(2)
                    elif player.plate == [False,True,False,False]:
                        player.pick_up(3)
                    elif player.plate == [False,False,True,False]:
                        player.pick_up(4)
                    elif player.plate == [False,False,False,True]:
                        player.pick_up(16)
                    elif player.plate == [True,True,False,False]:
                        player.pick_up(5)
                    elif player.plate == [True,False,True,False]:
                        player.pick_up(6)
                    elif player.plate == [False,True,True,False]:
                        player.pick_up(7)
                    elif player.plate == [True,False,False,True]:
                        player.pick_up(11)
                    elif player.plate == [False,True,False,True]:
                        player.pick_up(9)
                    elif player.plate == [False,False,True,True]:
                        player.pick_up(10)
                    elif player.plate == [True,True,True,False]:
                        player.pick_up(8)
                    elif player.plate == [True,True,False,True]:
                        player.pick_up(13)
                    elif player.plate == [True,False,True,True]:
                        player.pick_up(14)
                    elif player.plate == [False,True,True,True]:
                        player.pick_up(12)
                    elif player.plate == [True,True,True,True]:
                        player.pick_up(15)
                    else:
                        player.pick_up(1)



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



        

            # if stove is True:
            #     if pygame.time.get_ticks() - timer_list[-1] > 5000:
            #         world.blit(backdrop, backdropbox)
            #         stove_list.draw(world)
            #         print("da")


            if event.type == pygame.KEYDOWN:
                if event.key == ord('e'):
                    if 655 < player.rect.x < 800 and 300 < player.rect.y < 500:
                        if player.plate[2] is True and player.plate[3] is False and stove is False:
                            timer_list.append(pygame.time.get_ticks())
                            print(timer_list)
                            stove = True
                            print(f"start stove {stove}")
                            player.plate[2] = False   

                elif event.key == ord('f'):
                    if 635 < player.rect.x < 800 and 300 < player.rect.y < 500:
                        if pygame.time.get_ticks() - timer_list[-1] > 10000:
                            print("overcooked")
                            stove = False
                            player.plate[3] = False
                        elif 7000 < pygame.time.get_ticks() - timer_list[-1] <= 10000:
                            player.plate[3] = True
                            print("cooked")
                            stove = False
                        print(f'stove = {stove}')
                        print(player.plate)

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
        elif player.rect.x > 800 and 380 < player.rect.y < 510:
            player.rect.x = 780


    world.blit(backdrop, backdropbox)
    if counter >= 0:
        draw_timer(world, 860, 55, time_left())
        draw_money(world, 700, 55, player.geld)
        draw_recipe(world, 30, 55, recipes[player.recipe_counter])
    else:
        pygame.sprite.Sprite.kill(player)
        pop_ups_list.draw(world)
        draw_money(world, 540, 450, f"{player.geld}")

    player.update()  # update player position
    player_list.draw(world)  # draw player
    pygame.display.flip()
    clock.tick(FPS)

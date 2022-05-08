"""
Main file for running the game.
"""
import sys
import os
import pygame
from model import ModelCook
from view import ViewCook
from controller import ControllerCook



# Set up game window
WORLDX = 960
WORLDY = 720
world = pygame.display.set_mode([WORLDX, WORLDY])
backdrop = pygame.image.load(os.path.join('images', 'stage.png'))
backdropbox = world.get_rect()

# Set up the model for the whole game
model = ModelCook(world)
model.spritecook.rect.x = 0
model.spritecook.rect.y = 275
player_list = pygame.sprite.Group()
player_list.add(model.spritecook)

model.popup.rect.x = 280
model.popup.rect.y = 360
pop_ups_list = pygame.sprite.Group()
pop_ups_list.add(model.popup)

view = ViewCook(model)
controller = ControllerCook(model)

pygame.init()
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)
counter = model.time_left()

MAIN = True
FPS = 40

model.random_recipe()

while MAIN:
    for event in pygame.event.get():  # every time an event happens in pygame
        if event.type == pygame.USEREVENT:
            counter -= 1  # decrease the counter every second

        controller.key_press(event)
        view.player_appearance()

        if event.type == pygame.KEYUP:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                MAIN = False

    model.player_bounds()
    world.blit(backdrop, backdropbox)

    view.draw_money()
    view.draw_timer()
    view.draw_recipe()
    view.draw_cooker_timer()

    if counter < 0:
        model.end_game()
        pygame.sprite.Sprite.kill(model.spritecook)
        pop_ups_list.draw(world)  # draw pop up
        view.draw_money_end() # display final money count

    controller.update()  # update player position
    player_list.draw(world)  # draw player
    pygame.display.flip()
    clock.tick(FPS)

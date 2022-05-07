from model import ModelCook
from view import ViewCook
from controller import ControllerCook
import pygame
import sys
import os

WORLDX = 960
WORLDY = 720
BLACK = (23, 23, 23)
world = pygame.display.set_mode([WORLDX, WORLDY])
backdrop = pygame.image.load(os.path.join('images', 'stage.png'))
backdropbox = world.get_rect()

model = ModelCook(world)
model.spritecook.rect.x = 0
model.spritecook.rect.y = 275
player_list = pygame.sprite.Group()
player_list.add(model.spritecook)

view = ViewCook(model)
controller = ControllerCook(model)

pygame.init()
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)
counter = model.time_left()
print(counter)

MAIN = True
FPS = 40

while MAIN:
    for event in pygame.event.get(): #every time an event happens in pygame
        if event.type == pygame.USEREVENT:
            counter -= 1 #decrease the counter every second
            print(counter)

        controller.key_press(event)
        view.player_appearance()
        # if event.type == pygame.KEYDOWN and event.key == ord('a'):
        #     model.random_recipe()

        if event.type == pygame.KEYUP:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                MAIN = False
    world.blit(backdrop, backdropbox)
    controller.update()  # update player position
    player_list.draw(world)  # draw player
    pygame.display.flip()
    clock.tick(FPS)
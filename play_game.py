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

# Set up view and controller
view = ViewCook(model)
controller = ControllerCook(model)

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)
counter = model.time_left()

MAIN = True
FPS = 40

# Generate random recipes in the game
model.random_recipe()

while MAIN:
    for event in pygame.event.get():  # every time an event happens in pygame
        if event.type == pygame.USEREVENT:
            counter -= 1  # decrease the counter every second

        controller.key_press(event) # Call the function when a key is pressed
        view.player_appearance() # Check the icon of the player

    model.player_bounds() # Keep the player in bounds
    world.blit(backdrop, backdropbox) # Redraw the world background

    # Make visuals for the stats in game
    view.draw_money()
    view.draw_timer()
    view.draw_recipe()
    view.draw_cooker_timer()

    if counter < 0:
        model.end_game() # Adjust money for items in player hand
        pygame.sprite.Sprite.kill(model.spritecook) # Kill the sprite
        pop_ups_list.draw(world)  # draw pop up
        view.draw_money_end() # display final money count

    controller.update()  # update player position
    player_list.draw(world)  # draw player
    pygame.display.flip() # Update display
    clock.tick(FPS) # Move the clock

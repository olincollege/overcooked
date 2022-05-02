import os
import sys
import pygame
from model import ModelCook


class ViewCook(ModelCook):

    WORLDX = 960
    WORLDY = 720
    recipe_coord = (30, 55)
    timer_coord = (860, 55)
    money_coord = (700, 55)
    BLACK = (23, 23, 23)
    world = pygame.display.set_mode([WORLDX, WORLDY])
    backdrop = pygame.image.load(os.path.join('images', 'stage.png'))
    backdropbox = world.get_rect()
    
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1, 10):
            img = pygame.image.load(os.path.join(
                'images', 'hero' + str(i) + '.png')).convert()
            img.convert_alpha()     # optimise alpha
            img.set_colorkey(ALPHA)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()


    def draw_recipe(self, world, recipe):
        """
        Draws the recipes on the game screen
        """
        font = pygame.font.Font(None, 30)  # Choose the font for the text
        current_recipe = []
        for index, ingredient in enumerate(self.ingredients):
            if recipe[index] is True:
                current_recipe.append(ingredient)

        text = font.render(str(current_recipe), 1, self.BLACK)  # Create the text
        world.blit(text, self.recipe_coord)

    def draw_timer(self, world, left_time):
        """
        Draws the time on the game screen
        """

        font = pygame.font.Font(None, 60)  # Choose the font for the tex_coordt
        text = font.render(str(left_time), 1, self.BLACK)  # Create the text
        world.blit(text, self.timer_coord)  # Draw the text on the screen

    def draw_money(self, world, amount):
        """
        Draws the money on the game screen
        """
        font = pygame.font.Font(None, 60)  # Choose the font for the text
        text = font.render(str(amount), 1, self.BLACK)  # Create the text
        world.blit(text, self.money_coord)

    def change_player_appearance(self, color_num):
        """
        Change sprite color.
        """
        self.image = self.images[color_num]

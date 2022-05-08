import os
import sys
import pygame
from model import ModelCook


class ViewCook():

    def __init__(self, model: ModelCook):
        self.model = model
        self.recipe_coord = (30, 55)
        self.timer_coord = (860, 55)
        self.cooker_timer_coord = (850, 500)
        self.money_coord = (700, 55)
        self.money_coord_end = (540, 450)
        self.BLACK = (23, 23, 23)
        self.WHITE = (255, 255, 255)

    def draw_recipe(self):
        """
        Draws the recipes on the game screen
        """
        recipe = self.model._recipes[self.model._recipe_counter]
        font = pygame.font.Font(None, 30)  # Choose the font for the text
        current_recipe = []
        for index, ingredient in enumerate(self.model._ingredients):
            if recipe[index] is True:
                current_recipe.append(ingredient)
        text = font.render(str(current_recipe), 1,
                           self.BLACK)  # Create the text
        self.model.world.blit(text, self.recipe_coord)

    def draw_timer(self):
        """
        Draws the time on the game screen
        """
        left_time = self.model.time_left()
        font = pygame.font.Font(None, 60)  # Choose the font for the tex_coordt
        text = font.render(str(left_time), 1, self.BLACK)  # Create the text
        # Draw the text on the screen
        self.model.world.blit(text, self.timer_coord)

    def draw_cooker_timer(self):
        """
        Draws the time on the game scree4
        """
        if self.model._stove == True:
            elapsed_time = int(
                (pygame.time.get_ticks() - self.model.cooking_timer)/1000)
            # Choose the font for the tex_coord
            font = pygame.font.Font(None, 30)
            if elapsed_time < 5:
                text = font.render(str(elapsed_time), 1,
                                   self.BLACK)  # Create the text
            elif elapsed_time > 8:
                text = font.render(str('Overcooked'), 1,
                                   self.BLACK)  # Create the text
            else:
                # Create the text
                text = font.render(str('Done'), 1, self.BLACK)
            # Draw the text on the screen
            self.model.world.blit(text, self.cooker_timer_coord)

    def draw_money(self):
        """
        Draws the money on the game screen
        """
        font = pygame.font.Font(None, 60)  # Choose the font for the text
        text = font.render(str(self.model._geld), 1,
                           self.BLACK)  # Create the text
        self.model.world.blit(text, self.money_coord)

    def draw_money_end(self):
        """
        Draws the money at the end of the game.
        """
        font = pygame.font.Font(None, 60)  # Choose the font for the text
        text = font.render(str(self.model._geld), 1,
                           self.WHITE)  # Create the text
        self.model.world.blit(text, self.money_coord_end)

    def player_appearance(self):
        if self.model._plate == [True, False, False, False]:
            self.change_appearance(2)
        elif self.model._plate == [False, True, False, False]:
            self.change_appearance(3)
        elif self.model._plate == [False, False, True, False]:
            self.change_appearance(4)
        elif self.model._plate == [False, False, False, True]:
            self.change_appearance(16)
        elif self.model._plate == [True, True, False, False]:
            self.change_appearance(5)
        elif self.model._plate == [True, False, True, False]:
            self.change_appearance(6)
        elif self.model._plate == [False, True, True, False]:
            self.change_appearance(7)
        elif self.model._plate == [True, False, False, True]:
            self.change_appearance(11)
        elif self.model._plate == [False, True, False, True]:
            self.change_appearance(9)
        elif self.model._plate == [False, False, True, True]:
            self.change_appearance(10)
        elif self.model._plate == [True, True, True, False]:
            self.change_appearance(8)
        elif self.model._plate == [True, True, False, True]:
            self.change_appearance(13)
        elif self.model._plate == [True, False, True, True]:
            self.change_appearance(14)
        elif self.model._plate == [False, True, True, True]:
            self.change_appearance(12)
        elif self.model._plate == [True, True, True, True]:
            self.change_appearance(15)
        elif self.model._isplate == False:
            self.change_appearance(0)
        else:
            self.change_appearance(1)

    def change_appearance(self, sprite_num):
        """
        Change sprite appearance.
        """
        self.model.spritecook.image = self.model.spritecook.images[sprite_num]

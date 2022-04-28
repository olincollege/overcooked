"""
Helper functions that are used in pygame_main.py
"""
import random
import os
import pygame

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 0, 0)
ingredients = ["Strawberry", "Canteloup", "Grape"]


def random_recipe(num_recipes):
    """
    Generate random recipes represented by a list of binaries

    Args:
        num_recipes: an int of how many recipes that needs to be generated

    Returns:
        a list of list, which consists of three binaries showing if a fruit is
        present in the recipe

    """
    recipes = []
    for _ in range(num_recipes):
        recipe = []
        for _ in range(3):
            recipe.append(random.choice([True, False]))
        if sum(recipe) != 0:
            recipes.append(recipe)
    return recipes


def time_left():
    """
    Counts the time left in the game

    Returns:
        Time left in the game, in milliseconds

    """

    total_time_minutes = 0.1
    total_time_milli = (total_time_minutes*60)*1000
    time_left_milli = total_time_milli - pygame.time.get_ticks()
    left_time = int(time_left_milli/1000)
    if left_time <= 0:
        left_time = "0"

    return left_time


def draw_timer(world, x_coord, y_coord, left_time):
    """
    Draws the time on the game screen
    """

    font = pygame.font.Font(None, 60)  # Choose the font for the tex_coordt
    text = font.render(str(left_time), 1, BLACK)  # Create the text
    world.blit(text, (x_coord, y_coord))  # Draw the text on the screen


def draw_money(world, x_coord, y_coord, amount):
    """
    Draws the money on the game screen
    """
    font = pygame.font.Font(None, 60)  # Choose the font for the text
    text = font.render(str(amount), 1, BLACK)  # Create the text
    world.blit(text, (x_coord, y_coord))


def draw_recipe(world, x_coord, y_coord, recipe):
    """
    Draws the recipes on the game screen
    """
    font = pygame.font.Font(None, 30)  # Choose the font for the text
    current_recipe = []
    for index,ingredient in enumerate(ingredients):
        if recipe[index] is True:
            current_recipe.append(ingredient)

    text = font.render(str(current_recipe), 1, BLACK)  # Create the text
    world.blit(text, (x_coord, y_coord))


class PopUp(pygame.sprite.Sprite):
    """
    Creates pop up window at the end of the game
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(os.path.join('images', 'pop3.png')).convert()
        img.convert_alpha()     # optimise alpha
        img.set_colorkey(ALPHA)
        self._image = img
        self.rect = self.image.get_rect()

    @property
    def image(self):
        """
        Property
        """
        return self._image

    def additional_method(self):
        """
        additional method to make pylint happy
        """

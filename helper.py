import random
import pygame

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

    total_time_minutes = 2
    total_time_milli = (total_time_minutes*60)*1000
    time_left_milli =  total_time_milli - pygame.time.get_ticks()
    time_left = int(time_left_milli/1000)
    return time_left


def draw_timer(world, x, y, time_left):
    """
    Draws the time on the game screen
    """

    font = pygame.font.Font(None, 60) #Choose the font for the text
    text = font.render(str(time_left), 1, BLACK) #Create the text
    world.blit(text, (x, y)) #Draw the text on the screen

def draw_money(world, x, y, amount):
    """
    Draws the money on the game screen
    """    
    font = pygame.font.Font(None, 60) #Choose the font for the text
    text = font.render(str(amount), 1, BLACK) #Create the text
    world.blit(text, (x, y))


def draw_recipe(world, x, y, recipe):
    """
    Draws the recipes on the game screen
    """
    font = pygame.font.Font(None, 30) #Choose the font for the text
    current_recipe = []
    for i in range(len(ingredients)):
        if recipe[i] == True:
            current_recipe.append(ingredients[i])
        
    text = font.render(str(current_recipe), 1, BLACK) #Create the text
    world.blit(text, (x, y))
import random 
import pygame



class ModelCook(pygame.sprite.Sprite):

    def __init__(self):
        self._recipe_counter = 0
        self._ingredients = ["Strawberry", "Canteloupe", "Grape"]
        self._num_recipes = 20
        self._geld = 100
        self._isplate = False
        self._plate = [False, False, False]
        self._player_coord = [0,0]


    def random_recipe(self):
        """
        Generate random recipes represented by a list of binaries

        Args:
            num_recipes: an int of how many recipes that needs to be generated

        Returns:
            a list of list, which consists of three binaries showing if a fruit is
            present in the recipe

        """
        recipes = []
        for _ in range(self._num_recipes):
            recipe = []
            for _ in range(3):
                recipe.append(random.choice([True, False]))
            if sum(recipe) != 0:
                recipes.append(recipe)
        return recipes

    def time_left(self):
        """
        Counts the time left in the game

        Returns:
            Time left in the game, in milliseconds

        """

        total_time_minutes = 1
        total_time_milli = (total_time_minutes*60)*1000
        time_left_milli = total_time_milli - pygame.time.get_ticks()
        left_time = int(time_left_milli/1000)
        if left_time <= 0:
            left_time = "0"

        return left_time

    def toss(self):
        """
        Toss the plate and food and lose money
        """
        self._isplate = False
        # self.pick_up(0) put in view
        if sum(self._plate) == 3:
            self._geld -= 30
        elif sum(self._plate) == 2:
            self._geld -= 20
        elif sum(self._plate) == 1:
            self._geld -= 10
        self._plate = [False, False, False]

    def sell(self, recipes):
        """
        Sell the plate and food and gain money
        """
        self._isplate = False
        # self.pick_up(0)
        if self._plate == recipes[self.recipe_counter]:
            if sum(self._plate) == 3:
                self._geld += 30
            elif sum(self._plate) == 2:
                self._geld += 20
            elif sum(self._plate) == 1:
                self._geld += 10
            self._plate = [False, False, False]
            self._recipe_counter += 1

        else:
            self.toss()

    

    
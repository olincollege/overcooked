"""
defines all classes that make up the model of the game
"""
import random
import os
import pygame


class SpriteCook(pygame.sprite.Sprite):
    """
    Spawn a player and set up its icon

    Attributes:
    images: a list of all icons for the player
    image: individual icons
    """
    def __init__(self, world):
        self.world = world
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1, 18):
            img = pygame.image.load(os.path.join(
                'images', 'hero' + str(i) + '.png')).convert()
            img.convert_alpha()     # optimise alpha
            img.set_colorkey((0, 0, 0))  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()


class PopUp(pygame.sprite.Sprite):
    """
    Creates pop up window at the end of the game

    Attributes:
    image: the icons for end-of-game popups
    """

    def __init__(self, world):
        self.world = world
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(os.path.join('images', 'pop3.png')).convert()
        img.convert_alpha()     # optimise alpha
        img.set_colorkey((0, 0, 0))
        self.image = img
        self.rect = self.image.get_rect()


class ModelCook():
    """
    defines the length of the game, the recipes, the selling and tossing of
    food, the status of cooking, pick up and put down items
    Attributes:
    world: a pygame object that defines the game visuals
    _recipe_counter: an integer that counts the recipes used
    _ingredients: a list of all ingredients in the recipes
    _num_recipes: an int for the number of recipes randomly generated
    _geld: an int for the initial number of money
    _isplate: a binary representing if the player has a plate in hand
    _plate: a list of binaries showing if an ingredient is present in the plate
    _stove: a binary showing if the stove is occupied
    cooking_timer: an int that counts the cooking time
    _recipes: a list of recipes being used in the game
    _raisin: a binary of if raisin is in the plate
    STEP: an int showing how many pixels to move
    """

    def __init__(self, world):
        self.world = world
        self.spritecook = SpriteCook(world)
        self.popup = PopUp(world)
        self._recipe_counter = 0
        self._ingredients = ["Strawberry", "Canteloupe", "Grape", "Raisin"]
        self._num_recipes = 20
        self._geld = 100
        self._isplate = False
        self._plate = [False, False, False, False]
        self._stove = False  # whether there is something on the stove
        self.cooking_timer = 0
        self._recipes = []
        self._raisin = False

        self.STEP = 10  # how many pixels to move

    def random_recipe(self):
        """
        Generate random recipes represented by a list of binaries

        Args:
            num_recipes: an int of how many recipes that needs to be generated

        Returns:
            a list of list, which consists of three binaries showing if a fruit
            is present in the recipe

        """
        for _ in range(self._num_recipes):
            recipe = []
            for _ in range(4):
                recipe.append(random.choice([True, False]))
            if sum(recipe) != 0:
                self._recipes.append(recipe)

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
        if sum(self._plate) == 4:
            self._geld -= 40
        elif sum(self._plate) == 3:
            self._geld -= 30
        elif sum(self._plate) == 2:
            self._geld -= 20
        elif sum(self._plate) == 1:
            self._geld -= 10
        self._plate = [False, False, False, False]
        self._raisin = False

    def sell(self):
        """
        Sell the plate and food and gain money
        """
        self._isplate = False
        if self._plate == self._recipes[self._recipe_counter]:
            if sum(self._plate) == 4:
                self._geld += 40
            if sum(self._plate) == 3:
                self._geld += 30
            elif sum(self._plate) == 2:
                self._geld += 20
            elif sum(self._plate) == 1:
                self._geld += 10
            self._plate = [False, False, False, False]
            self._raisin = False
            self._recipe_counter += 1

        else:
            self.toss()

    def pick_up_item(self):
        """
        pick up an ingredient and put it into plate
        """
        if 50 < self.spritecook.rect.x < 250 and self.spritecook.rect.y > 500:
            # if the player is at the plate station
            self._isplate = True  # player has a plate
            # view.player_appearance() # update the player image
        if self._isplate:  # if the player is holding a plate
            # if the player is at the first ingredient station
            if (50 < self.spritecook.rect.x < 250
            and self.spritecook.rect.y < 315):
                # if they are not currently holding this ingredient
                if self._plate[0] is False:
                    self._plate[0] = True  # give them the ingredient

            elif (355 < self.spritecook.rect.x < 600
            and self.spritecook.rect.y < 315):
                # second ingredient station
                if self._plate[1] is False:
                    self._plate[1] = True

            elif (655 < self.spritecook.rect.x < 910
            and self.spritecook.rect.y < 315):
                # third ingredient station
                if self._plate[2] is False:
                    self._plate[2] = True
                    print(self._plate[2])
        else:
            print('You need a plate.')

        if (635 < self.spritecook.rect.x < 800
        and 300 < self.spritecook.rect.y < 500):
            if self._stove is True and self._isplate is True:
                self.how_cooked()
                self._stove = False

    def how_cooked(self):
        """
        tests if the raisin is undercooked, well-cooked, or overcooked
        """
        elapsed_time = (pygame.time.get_ticks() - self.cooking_timer)/1000
        if elapsed_time < 5:
            self._geld -= 10
        elif elapsed_time > 5 and elapsed_time < 8:
            self._plate[3] = True
        elif elapsed_time > 8:
            self._geld -= 10

        self.cooking_timer = 0

    def put_down_item(self):
        """
        put a plate down to cook, trash or sell
        """
        if (760 < self.spritecook.rect.x < 910
        and self.spritecook.rect.y > 500):
            self.toss()

        elif (355 < self.spritecook.rect.x < 655
        and self.spritecook.rect.y > 500):
            self.sell()

        elif (655 < self.spritecook.rect.x < 800
        and 300 < self.spritecook.rect.y < 500):
            if (self._plate[2] is True
            and self._plate[3] is False
            and self._stove is False):
                self.cooking_timer = pygame.time.get_ticks()
                self._stove = True
                self._plate[2] = False

    def player_bounds(self):
        """
        set up the boundary that the player can move in
        """
        if self.spritecook.rect.x < 0:
            self.spritecook.rect.x = 0
        elif self.spritecook.rect.x > 900:
            self.spritecook.rect.x = 900
        elif self.spritecook.rect.y < 275:
            self.spritecook.rect.y = 275
        elif self.spritecook.rect.y > 536:
            self.spritecook.rect.y = 536
        elif (self.spritecook.rect.x > 800
        and 380 < self.spritecook.rect.y < 510):
            self.spritecook.rect.x = 780

    def end_game(self):
        """
        tosses everything at the end of the game
        """
        if self._stove is True:
            self._geld -= 10
            self._stove = False
        if self._plate != [False, False, False, False]:
            self.toss()

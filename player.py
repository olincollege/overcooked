"""
Player file.
"""
import pygame
import sys
import os

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

class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        self.movex = 0 # move along X
        self.movey = 0 # move along Y
        self.frame = 0 # count frames
        self.isplate = False
        self.plate = [False,False,False]
        self.geld = 100
#        self.recipes = random_recipe(10)
        self.recipe_counter = 0
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1, 10):
            img = pygame.image.load(os.path.join('images', 'hero' + str(i) + '.png')).convert()
            img.convert_alpha()     # optimise alpha
            img.set_colorkey(ALPHA) # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
    
    def control(self,x,y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y
    
    def update(self):
        """
        Update sprite position
        """
        self.rect.x = self.rect.x + self.movex   
        self.rect.y = self.rect.y + self.movey
    
    def pick_up(self, color_num):
        """
        Change sprite color.
        """
        self.image = self.images[color_num]
    
    def toss(self):
        self.isplate = False
        self.pick_up(0)
        if sum(self.plate) == 3:
            self.geld -= 30
        elif sum(self.plate) == 2:
            self.geld -= 20
        elif sum(self.plate) == 1:
            self.geld -= 10
        self.plate = [False,False,False]


    def sell(self,recipes):
        self.isplate = False
        self.pick_up(0)
        if self.plate == recipes[self.recipe_counter]:
            if sum(self.plate) == 3:
                self.geld += 30
            elif sum(self.plate) == 2:
                self.geld += 20
            elif sum(self.plate) == 1:
                self.geld += 10           
            self.plate = [False,False,False]
            self.recipe_counter += 1

        else:
            self.toss()

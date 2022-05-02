"""
Player file.
"""

import os
import pygame

ALPHA = (0, 0, 0)



class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        self.move = [0,0]  # move along X
        self.frame = 0  # count frames
        self.isplate = False
        self.plate = [False, False, False]
        
        self.recipe_counter = 0
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1, 10):
            img = pygame.image.load(os.path.join(
                'images', 'hero' + str(i) + '.png')).convert()
            img.convert_alpha()     # optimise alpha
            img.set_colorkey(ALPHA)  # set alpha
            self.images.append(img)
            

    def draw_player(self):
        self.image = self.images[0]
        self.rect = self.image.get_rect()


    def control(self, x_coord, y_coord):
        """
        control player movement
        """
        self.move[0] += x_coord
        self.move[1] += y_coord

    def update(self):
        """
        Update sprite position
        """
        self.rect.x = self.rect.x + self.move[0]
        self.rect.y = self.rect.y + self.move[1]

    def pick_up(self, color_num):
        """
        Change sprite color.
        """
        self.image = self.images[color_num]

    def toss(self):
        """
        Toss the plate and food and lose money
        """
        self.isplate = False
        self.pick_up(0)
        if sum(self.plate) == 3:
            self.geld -= 30
        elif sum(self.plate) == 2:
            self.geld -= 20
        elif sum(self.plate) == 1:
            self.geld -= 10
        self.plate = [False, False, False]

    def sell(self, recipes):
        """
        Sell the plate and food and gain money
        """
        self.isplate = False
        self.pick_up(0)
        if self.plate == recipes[self.recipe_counter]:
            if sum(self.plate) == 3:
                self.geld += 30
            elif sum(self.plate) == 2:
                self.geld += 20
            elif sum(self.plate) == 1:
                self.geld += 10
            self.plate = [False, False, False]
            self.recipe_counter += 1

        else:
            self.toss()

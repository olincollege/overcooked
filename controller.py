import pygame

class ControllerCook(ModelCook):

    def __init__():
        pass

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
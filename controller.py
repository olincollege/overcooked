import pygame
import sys
from model import ModelCook

class ControllerCook():

    def __init__(self, model:ModelCook):
        self.model = model
        self.move = [0, 0]

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
        self.model.spritecook.rect.x = self.model.spritecook.rect.x + self.move[0]
        self.model.spritecook.rect.y = self.model.spritecook.rect.y + self.move[1]
    
    def key_press(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                self.control(-self.model.STEP, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                self.control(self.model.STEP, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                self.control(0, -self.model.STEP)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                self.control(0, self.model.STEP)
                
            if event.key == ord('f'):
                self.model.pick_up_item()
            
            if event.key == ord('e'):
                self.model.put_down_item()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                self.control(self.model.STEP, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                self.control(-self.model.STEP, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                self.control(0, self.model.STEP)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                self.control(0, -self.model.STEP)

            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
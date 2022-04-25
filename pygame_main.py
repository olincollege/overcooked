# # define a main function
# def main():

#     # initialize the pygame module
#     pygame.init()
#     # load and set the logo
#     logo = pygame.image.load("logo32x32.png")
#     pygame.display.set_icon(logo)
#     pygame.display.set_caption("minimal program")

#     # create a surface on screen that has the size of 240 x 180
#     screen = pygame.display.set_mode((240,180))

#     # define a variable to control the main loop
#     running = True

#     # main loop
#     while running:
#         # event handling, gets all event from the event queue
#         for event in pygame.event.get():
#             # only do something if the event is of type QUIT
#             if event.type == pygame.QUIT:
#                 # change the value to False, to exit the main loop
#                 running = False


# # run the main function only if this module is executed as the main script
# # (if you import this as a module then nothing is executed)
# if name=="main":
#     # call the main function
#     main()
import pygame
import sys
import os

'''
Variables
'''
worldx = 960
worldy = 720
fps   = 40  # frame rate
ani   = 4   # animation cycles
BLUE  = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
main = True


'''
Objects
'''

class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        self.movex = 0 # move along X
        self.movey = 0 # move along Y
        self.frame = 0 # count frames
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1, 3):
            img = pygame.image.load(os.path.join('images', 'hero' + str(i) + '.png')).convert()
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

'''
Setup
'''

clock = pygame.time.Clock()
pygame.init()
# world = pygame.display.set_mode([worldx, worldy])

world = pygame.display.set_mode([worldx,worldy])
backdrop = pygame.image.load(os.path.join('images','stage.png'))
backdropbox = world.get_rect()

player = Player()   # spawn player
player.rect.x = 0   # go to x
player.rect.y = 0   # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10  # how many pixels to move
# world = pygame.display.set_mode([worldx,worldy])
# backdrop = pygame.image.load(os.path.join('images','stage.png'))
# backdropbox = world.get_rect()


'''
Main loop
'''

while main:
    for event in pygame.event.get():
        # if event.type == pygame.QUIT:
        #     pygame.quit()
        #     try:
        #         sys.exit()
        #     finally:
        #         main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0,-steps)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, steps)
            if  event.key == ord('f'):
                if player.rect.x == 0 and player.rect.y == 0:
                    player.pick_up(0)
                else:
                    player.pick_up(1)
            

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0, steps)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, -steps)
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False  

    # world.fill(BLUE)
    world.blit(backdrop, backdropbox)
    player.update()  # update player position
    player_list.draw(world) # draw player
    pygame.display.flip()
    clock.tick(fps)

# while main:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit(); sys.exit()
#             main = False

#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT or event.key == ord('a'):
#                 print('left')
#             if event.key == pygame.K_RIGHT or event.key == ord('d'):
#                 print('right')
#             if event.key == pygame.K_UP or event.key == ord('w'):
#             print('jump')

#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT or event.key == ord('a'):
#                 print('left stop')
#             if event.key == pygame.K_RIGHT or event.key == ord('d'):
#                 print('right stop')
#             if event.key == ord('q'):
#                 pygame.quit()
#                 sys.exit()
#                 main = False 
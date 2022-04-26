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
ALPHA = (0, 0, 0)
main = True
money = 0


'''
Objects
'''
start_time = pygame.time.get_ticks() 
def time_left():
    total_time_minutes = 2
    total_time_milli = (total_time_minutes*60)*1000
    time_left_milli =  total_time_milli - pygame.time.get_ticks()
    time_left = int(time_left_milli/1000)
    return time_left

def draw_timer(world, x, y, time_left):
    font = pygame.font.Font(None, 60) #Choose the font for the text
    text = font.render(str(time_left), 1, BLACK) #Create the text
    world.blit(text, (x, y)) #Draw the text on the screen

def draw_money(world, x, y, amount):
    font = pygame.font.Font(None, 60) #Choose the font for the text
    text = font.render(str(amount), 1, BLACK) #Create the text
    world.blit(text, (x, y))

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

'''
Setup
'''

clock = pygame.time.Clock()
pygame.init()
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

    world.blit(backdrop, backdropbox)
    draw_timer(world, 860, 55, time_left())
    draw_money(world, 700, 55, money)
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
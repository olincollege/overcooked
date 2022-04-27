from prompt_toolkit import print_formatted_text
import pygame
import sys
import os
import random

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

#recipe = [[True,False,True],[True,True,True]]
ingredients = ["Strawberry","Canteloup","Grape"]

'''
Objects
'''
start_time = pygame.time.get_ticks()

def random_recipe(num_recipes):
    recipes = []
    for _ in range(num_recipes):
        recipe = []
        for _ in range(3):
            recipe.append(random.choice([True, False]))
        if sum(recipe) != 0:
            recipes.append(recipe)
    return recipes
recipes = random_recipe(10)
print(f"real recipe{recipes}")

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


def draw_recipe(world, x, y, recipe):
    font = pygame.font.Font(None, 30) #Choose the font for the text
    current_recipe = []
    for i in range(len(ingredients)):
        if recipe[i] == True:
            current_recipe.append(ingredients[i])
        
    text = font.render(str(current_recipe), 1, BLACK) #Create the text
    world.blit(text, (x, y))



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
        print(recipes[0])
        print("tossed")

    def sell(self,recipes):
        self.isplate = False
        self.pick_up(0)
        if self.plate == recipes[self.recipe_counter]:
            if sum(self.plate) == 3:
                player.geld += 30
            elif sum(player.plate) == 2:
                player.geld += 20
            elif sum(player.plate) == 1:
                player.geld += 10
            #recipes = recipes[1:]
            print(f"after removal {recipes}")
            self.plate = [False,False,False]
            print("sold")
            self.recipe_counter += 1

        else:
            self.toss()

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
player.rect.y = 275   # go to y
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


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                player.control(0,-steps)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                player.control(0, steps)
            
            if event.key == ord('f'):
                if 50 < player.rect.x < 250 and player.rect.y > 500:
                    player.isplate = True
                    player.pick_up(1)


                if player.isplate:
                    if 50 < player.rect.x < 250 and player.rect.y < 315:
                        if player.plate[0] == False:
                            player.plate[0] = True
                            if player.plate[1] == False and player.plate[2] == False:
                                player.pick_up(2)
                            elif player.plate[1] == True and player.plate[2] == False:
                                player.pick_up(5)
                            elif player.plate[1] == True and player.plate[2] == True:
                                player.pick_up(6)
                            else:
                                player.pick_up(8)

                    elif 355 < player.rect.x < 600 and player.rect.y < 315:
                        if player.plate[1] == False:
                            player.plate[1] = True
                            if player.plate[0] == False and player.plate[2] == False:
                                player.pick_up(3)
                            elif player.plate[0] == True and player.plate[2] == False:
                                player.pick_up(5)
                            elif player.plate[0] == False and player.plate[2] == True:
                                player.pick_up(7)
                            else:
                                player.pick_up(8)  

                    elif 655 < player.rect.x < 910 and player.rect.y < 315:
                        if player.plate[2] == False:
                            player.plate[2] = True
                            if player.plate[0] == False and player.plate[1] == False:
                                player.pick_up(4)
                            elif player.plate[0] == True and player.plate[1] == False:
                                player.pick_up(6)
                            elif player.plate[0] == False and player.plate[1] == True:
                                player.pick_up(7)
                            else:
                                player.pick_up(8)
                    else:
                        pass
                else: 
                    print("you need a plate")

            if event.key == ord('e'):
                if 760 < player.rect.x < 910 and player.rect.y > 500:
                    player.toss()

                elif 355 < player.rect.x < 655 and player.rect.y > 500:
                    player.sell(recipes)

               
            

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

        if player.rect.x < 0:
            player.rect.x = 0
        elif player.rect.x > 900:
            player.rect.x = 900
        elif player.rect.y < 275:
            player.rect.y = 275
        elif player.rect.y > 536:
            player.rect.y = 536

    world.blit(backdrop, backdropbox)
    draw_timer(world, 860, 55, time_left())
    draw_money(world, 700, 55, player.geld)
    draw_recipe(world, 30, 55, recipes[player.recipe_counter])
    player.update()  # update player position
    player_list.draw(world) # draw player
    pygame.display.flip()
    clock.tick(fps)
    if time_left == 0:
        pygame.quit()
        sys.exit()

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
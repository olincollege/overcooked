"""
Main game file.
"""
#create board
board = Board()

#create player
player = Player()

#create money
money = Money()

#create dishes
dish = Dish()

def play():
    while time > 0: 
        move() #move checks if there is move input and moves the player
        if in_region == str() and player_input == 'f': #if the player is in a region and press the action button (f)
            if player.holding == True: # if the player is holding something already
                if in_region == 'serve': # if they are in the serve region
                player.put_down() # put down the players hand
                # add something to check if the player served the right dish here
                money.add_money() # get money 
                dish.remove_dish() # remove the dish from the current dishes

                if in_region == 'trash': # if they are in the trash region
                    player.put_down() # put down the players hand
                    money.remove_money() # lose money

                if in_region in ingredients and player_dict['plate'] == True: # if the player is in range of an ingredient and is holding a plate
                    player.pick_up(in_region) # pick up the ingredient

            elif player.holding == False and in_region == 'plate': # if the player is not holding something and in the plate region
                pick_up(in_region) # pick up a plate
        board() #update the board
    return "Time is up!"




            
                
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
        move()
        if in_region == str() and player_input == 'f':
            if player.holding == True:
                if in_region == 'serve':
                player.put_down()
                money.add_money()
                dish.remove_dish()

                if in_region == 'trash':
                    player.put_down()
                    money.remove_money()

                if in_region in ingredients:
                    player.pick_up(in_region)

            elif player.holding == False and in_region == 'plate':
                pick_up(in_region)
            
                
"""
Player file.
"""

class Player:
    #need to inherit region boundaries from board

    def __init__(self):
        #need to inherit ingredients from board
        player_info = {'location': (0,0), ingredient_1: False, ingredient_2: False, ingredient_3: False, 'plate': False, 'money': 0}

    def move(self, new_location):
        pass

    # def pick_up(self, item):
    #     pass
    
    # def put_down(self):
    #     pass

    # def in_region(self, current_location):
    #     pass
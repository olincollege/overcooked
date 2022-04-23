"""
Board file.
"""
class Board:
    ingredient_1 = 'Strawberry'
    ingredient_2 = 'Cantaloupe'
    ingredient_3 = 'Grape'
    ingredients = [ingredient_1, ingredient_2, ingredient_3]

    #add regions here

class player_region(Board):
    pass

class status_region(Board):

    def update_status(self):
        pass
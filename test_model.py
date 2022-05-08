import pytest
import pygame
from model import ModelCook

WORLDX = 960
WORLDY = 720
world = pygame.display.set_mode([WORLDX, WORLDY])

toss = [
    (world, [True, False, True, False], 80),
    (world, [True, False, False, False], 90),

]

sell = [
    (world, [True, False, True, False], [[True, False, True, False], [True, False, False, False]], 0, 120),
    (world, [True, False, False, False], [[True, False, True, False], [True, False, False, False]], 1, 110),
]

pick_up_item = [
    (world, 60, 310, 0),
    (world, 360, 310, 1),
    (world, 660, 310, 2),
]

put_down_item = [
    (world, 770, 510, [True, False, False, False], [[True, False, False, False]], 90),
    (world, 360, 510, [True, False, False, False], [[True, False, False, False]], 110),
    (world, 360, 510, [True, False, False, False], [[True, True, False, False]], 90),
]

@pytest.mark.parametrize("world, plate, geld", toss)
def test_toss(world, plate, geld):
    pygame.init()
    test = ModelCook(world)
    test._plate = plate
    test.toss()
    assert test._geld == geld
    assert test._raisin == False
    assert test._isplate == False
    assert test._plate == [False, False, False, False]

@pytest.mark.parametrize("world, plate, recipes, recipe_counter, geld", sell)
def test_sell(world, plate, recipes, recipe_counter, geld):
    pygame.init()
    test = ModelCook(world)
    test._plate = plate
    test._recipe_counter = recipe_counter
    test._recipes = recipes
    test.sell()
    assert test._geld == geld
    assert test._raisin == False
    assert test._isplate == False
    assert test._plate == [False, False, False, False]

@pytest.mark.parametrize("world, x_coord, y_coord, ingredient_num", pick_up_item)
def test_pick_up_item(world, x_coord, y_coord, ingredient_num):
    pygame.init()
    test = ModelCook(world)
    test.spritecook.rect.x = x_coord
    test.spritecook.rect.y = y_coord
    test._isplate = True
    test.pick_up_item()
    assert test._plate[ingredient_num] == True

@pytest.mark.parametrize("world, x_coord, y_coord, plate, recipe, geld", put_down_item)
def test_put_down_item(world, x_coord, y_coord, plate, recipe, geld):
    pygame.init()
    test = ModelCook(world)
    test.spritecook.rect.x = x_coord
    test.spritecook.rect.y = y_coord
    test._isplate = True
    test._plate = plate
    test._recipe_counter = 0
    test._recipes = recipe
    test.put_down_item()
    assert test._plate == [False, False, False, False]
    assert test._isplate == False
    assert test._geld == geld
    

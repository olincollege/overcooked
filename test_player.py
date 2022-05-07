import pytest
import pygame
from player import Player

control = [
    (10, 10, [10, 10]),
    (20, 0, [20, 0]),
]

update = [
    (10, 10, [10, 10]),
    (20, 0, [20, 0]),
]

toss = [
    ([True, False, True, False], 80),
    ([True, False, False, False], 90),

]

sell = [
    ([True, False, True, False], [[True, False, True, False], [True, False, False, False]], 0, 120),
    ([True, False, False, False], [[True, False, True, False], [True, False, False, False]], 1, 110),
]


@pytest.mark.parametrize("x_coord, y_coord, move_out", control)
def test_control(x_coord, y_coord, move_out):
    pygame.init()
    pygame.display.set_mode([960, 720])
    player_test = Player()
    player_test.control(x_coord, y_coord)
    assert player_test.move == move_out

@pytest.mark.parametrize("x_coord, y_coord, move_out", update)
def test_update(x_coord, y_coord, move_out):
    pygame.init()
    pygame.display.set_mode([960, 720])
    player_test = Player()
    player_test.control(x_coord, y_coord)
    player_test.update()
    assert player_test.rect.x == move_out[0]
    assert player_test.rect.y == move_out[1]

@pytest.mark.parametrize("plate, geld", toss)
def test_toss(plate, geld):
    pygame.init()
    pygame.display.set_mode([960, 720])
    player_test = Player()
    player_test.plate = plate
    player_test.toss()
    assert player_test.geld == geld
    assert player_test.raisin == False
    assert player_test.isplate == False
    assert player_test.plate == [False, False, False, False]

@pytest.mark.parametrize("plate, recipes, recipe_counter, geld", sell)
def test_sell(plate, recipes, recipe_counter, geld):
    pygame.init()
    pygame.display.set_mode([960, 720])
    player_test = Player()
    player_test.plate = plate
    player_test.recipe_counter = recipe_counter
    player_test.sell(recipes)
    assert player_test.geld == geld
    assert player_test.raisin == False
    assert player_test.isplate == False
    assert player_test.plate == [False, False, False, False]
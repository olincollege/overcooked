import pytest
import pygame
from model import ModelCook

WORLDX = 960
WORLDY = 720
world = pygame.display.set_mode([WORLDX, WORLDY])

toss = [
    (world, [True, False, True, False], 80),  # test that tossing a plate with
    # two items removes 20 dollars
    (world, [True, False, False, False], 90),  # test that tossing a plate with
    # one item removes 10 dollars
    # test that tossing an empty plate
    (world, [False, False, False, False], 100),
    # doesn't take away any money
]

sell = [
    (world, [True, False, True, False], [[True, False, True, False],
    [True, False, False, False]], 0, 100, 120),  # test that selling the
    # correct recipe at recipe counter 0 adds the right amount of money
    (world, [True, False, False, False], [[True, False, True, False],
    [True, False, False, False]], 1, 100, 110),  # test that selling the
    # correct recipe at recipe counter 1 adds the right amount of money
    (world, [True, True, False, False], [[True, False, True, False],
    [True, False, False, False]], 1, 0, -20),  # test that selling the
    # correct recipe at the wrong recipe counter removes the right amount
    # of money
]

pick_up_item = [
    (world, 60, 310, 0),  # test that the player can pick up a strawberry
    (world, 360, 310, 1),  # test that the player can pick up a canteloupe
    (world, 660, 310, 2),  # test that the player can pick up a grape
]

pick_up_item_stove = [
    (world, 660, 450, True, False, [False, False, False, False],
     [False, False, False, False], True),  # test that the player can't pick up the
    # raisin when it is undercooked
    # DESIRED UNIT TEST;
    # test that the player can pick up a done raisin
    # test that an overdone raisin trashes when the player picks it up
    # test that the player cannot pick up a a raisin when out of range
    # test that the player cannot pick up a raisin if they are already
    # holding one
    # test that a player cannot pick up a raisin if they don't have a
    # plate
    # I can't figure out how to make these unit tests because it would involve
    # manually modifying the pygame time stamp which I don't know how to do.
    (world, 660, 450, False, False, [False, False, True, False],
    [False, False, True, False], True),  # test that the player can't pick up an
    # item if the stove is not engaged
]

pick_up_item_plate = [
    (world, 60, 600, True),  # test that the player can pick up a plate when
    # in range
    (world, 30, 600, False),  # test that the player cannot pick up a plate
    # when out of range
]

put_down_item = [
    (world, 770, 510, [True, False, False, False],
    [[True, False, False, False]], 90),  # test that the player can toss
    # a plate
    (world, 360, 510, [True, False, False, False],
    [[True, False, False, False]], 110),  # test that the player can sell
    # a correct plate
    (world, 360, 510, [True, False, False, False],
    [[True, True, False, False]], 90),  # test that the player cannot
    # sell an incorrect plate (plate gets tossed at sell station)
]

put_down_item_stove = [
    (world, 660, 450, True, True, [False, False, True, False],
    [False, False, True, False]),  # test that you cannot use the stove when it
    # is already on
    (world, 660, 450, False, True, [False, False, True, False],
    [False, False, False, False]),  # test that you can use the stove when
    # all factors are met
    (world, 660, 450, False, True, [True, False, True, False],
    [True, False, False, False]),  # test that you can use the stove when
    # all factors are met and you have extra ingredients
    (world, 660, 450, False, True, [True, False, True, True],
    [True, False, False, True]),  # test that you can use the stove when
    # all factors are met and you have extra ingredients including a
    # raisin
    (world, 654, 450, False, False, [False, False, True, False],
    [False, False, True, False]),  # test that you cannot use the stove if you
    # are out of range
    (world, 654, 450, False, False, [True, False, False, False],
     [True, False, False, False]),  # test that you cannot use the stove if you
    # do not have a grape
]

player_bounds = [
    (world, [-10, 20], [0, 275]),  # test that a player in the negative out of
    # bounds is returned correctly
    (world, [2000, 1000], [900, 536]),  # test that a player in the positive
    # out of bounds is returned correctly
    (world, [0, 1000], [0, 536]),  # test that a player out of bounds in one
    # dimension is returned correctly
    (world, [300, 400], [300, 400]),  # test that a player in bounds is not
    # moved
]

end_game = [
    # test that a player loses the
    (world, [True, False, False, False], 80, True),
    # correct amount of money at the end of the game with 1 ingredient on
    # their plate and the stove on
    # test with four ingredients on
    (world, [True, True, True, True], 50, True),
    # their plate and the stove on
    (world, [False, False, False, False], 90, True),  # test with an empty
    # plate and the stove on
    (world, [False, False, False, False], 100, False),  # test with an empty
    # plate and the stove off
    (world, [True, False, False, False], 90, False),  # test with 1 ingredient
    # and the stove off
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


@pytest.mark.parametrize("world, plate, recipes, recipe_counter, geld_in, geld_out", sell)
def test_sell(world, plate, recipes, recipe_counter, geld_in, geld_out):
    pygame.init()
    test = ModelCook(world)
    test._plate = plate
    test._recipe_counter = recipe_counter
    test._recipes = recipes
    test._geld = geld_in
    test.sell()
    assert test._geld == geld_out
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


@pytest.mark.parametrize("world, x_coord, y_coord, plate_out", pick_up_item_plate)
def test_pick_up_item_plate(world, x_coord, y_coord, plate_out):
    pygame.init()
    test = ModelCook(world)
    test.spritecook.rect.x = x_coord
    test.spritecook.rect.y = y_coord
    test.pick_up_item()
    assert test._isplate == plate_out


@pytest.mark.parametrize("world, x_coord, y_coord, stove_in, stove_out, plate_in, plate_out, isplate", pick_up_item_stove)
def test_pick_up_item_stove(world, x_coord, y_coord, stove_in, stove_out, plate_in, plate_out, isplate):
    pygame.init()
    test = ModelCook(world)
    test.spritecook.rect.x = x_coord
    test.spritecook.rect.y = y_coord
    test._isplate = isplate
    test._stove = stove_in
    test._plate = plate_in
    test.pick_up_item()
    assert test._stove == stove_out
    assert test._plate == plate_out


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


@pytest.mark.parametrize("world, x_coord, y_coord, stove_in, stove_out, plate_in, plate_out", put_down_item_stove)
def test_put_down_item_stove(world, x_coord, y_coord, stove_in, stove_out, plate_in, plate_out):
    pygame.init()
    test = ModelCook(world)
    test.spritecook.rect.x = x_coord
    test.spritecook.rect.y = y_coord
    test._isplate = True
    test._plate = plate_in
    test._stove = stove_in
    test.put_down_item()
    assert test._plate == plate_out
    assert test._stove == stove_out


@pytest.mark.parametrize("world, coord_in, coord_out", player_bounds)
def test_player_bounds(world, coord_in, coord_out):
    pygame.init()
    test = ModelCook(world)
    test.spritecook.rect.x = coord_in[0]
    test.spritecook.rect.y = coord_in[1]
    test.player_bounds()
    assert test.spritecook.rect.x == coord_out[0]
    assert test.spritecook.rect.y == coord_out[1]


@pytest.mark.parametrize("world, plate, end_geld, stove", end_game)
def test_end_game(world, plate, end_geld, stove):
    pygame.init()
    test = ModelCook(world)
    test._stove = stove
    test._plate = plate
    test.end_game()
    assert test._geld == end_geld

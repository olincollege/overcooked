import pytest
import pygame
from controller import ControllerCook
from model import ModelCook

WORLDX = 960
WORLDY = 720
world = pygame.display.set_mode([WORLDX, WORLDY])

control = [
    (world, 10, 10, [10, 10]), # test a player move when both x and y move
    (world, 20, 0, [20, 0]), # test a player move when only x moves
    (world, 0, 20, [0, 20]), # test a player move when only y moves
]

update = [
    (world, 0, 10, [0, 10]), # test that the player position is updated
    # when only y moves
    (world, 10, 0, [10, 0]), # test that the player position is updated
    # when only x moves
    (world, 30, 30, [30, 30]), # test that the player position is updated
    # when both x and y move
]

@pytest.mark.parametrize("world, x_coord, y_coord, move_out", control)
def test_control(world, x_coord, y_coord, move_out):
    pygame.init()
    model = ModelCook(world)
    test = ControllerCook(model)
    test.control(x_coord, y_coord)
    assert test.move == move_out
    
@pytest.mark.parametrize("world, x_coord, y_coord, move_out", update)
def test_update(world, x_coord, y_coord, move_out):
    pygame.init()
    model = ModelCook(world)
    test = ControllerCook(model)
    test.control(x_coord, y_coord)
    test.update()
    assert test.model.spritecook.rect.x == move_out[0]
    assert test.model.spritecook.rect.y == move_out[1]

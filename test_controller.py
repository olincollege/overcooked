import pytest
import pygame
from controller import ControllerCook
from model import ModelCook

WORLDX = 960
WORLDY = 720
world = pygame.display.set_mode([WORLDX, WORLDY])

control = [
    (world, 10, 10, [10, 10]),
    (world, 20, 0, [20, 0]),
]

update = [
    (world, 0, 10, [0, 10]),
    (world, 30, 30, [30, 30]),
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

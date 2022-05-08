import pytest
import pygame
from controller import ControllerCook
from model import ModelCook

control = [
    (10, 10, [10, 10]),
    (20, 0, [20, 0]),
]


@pytest.mark.parametrize("x_coord, y_coord, move_out", control)
def test_control(x_coord, y_coord, move_out):
    pygame.init()
    pygame.display.set_mode([960, 720])
    test = ControllerCook()
    test.control(self, x_coord, y_coord)
    assert test.move == move_out

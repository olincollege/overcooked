import pytest

from player import (
    random_recipe, 
    time_left,
    draw_timer,
    draw_money,
    draw_recipe,
)

# Define sets of test cases.
draw_timer = [
    ("input", "output")
]


@pytest.mark.parametrize("world, x_coord, y_coord, time_left", draw_timer)
def test_check_special_cases(world, x_coord, y_coord, time_left):
    '''
    Test that the function draw timer correctly draws the int given by the
    input time_left.

    Args:
        world:
        x_coord: an int representing the x coordinate of the top corner of the
        text
        y_coord: an int representing the y coordinate of the top corner of the
        text
        time_left: an int representing the amount of time left in the game
    '''
    assert pass
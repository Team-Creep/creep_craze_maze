from creep_craze_maze.creep_craze_maze import *

wall = Wall(400, 800, 20, 20, WHITE)

def test_rect_x():
    actual = wall.rect.x
    expected = 400
    assert actual == expected

def test_rect_y():
    actual = wall.rect.y
    expected = 800
    assert actual == expected

def test_rect_width():
    actual = wall.rect.width
    expected = 20
    assert actual == expected

def test_rect_height():
    actual = wall.rect.height
    expected = 20
    assert actual == expected


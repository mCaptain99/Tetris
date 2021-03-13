from block import Direction
from container import Container
import pytest


def test_new_block_when_floor():
    container = Container(10, 10)
    prev_block = container.block
    prev_pieces = prev_block.pieces[:]
    container.move_block(Direction.DOWN)
    assert prev_block is container.block
    assert prev_pieces != container.block.pieces
    for i in range(10):
        container.move_block(Direction.DOWN)
    assert prev_block != container.block
    for piece in prev_block.pieces:
        assert piece in container.floor
    for piece in container.block.pieces:
        assert piece not in container.floor


def test_check_if_layer_filled():
    container = Container(10, 10)
    container.floor.extend([(x, 1) for x in range(10)] + [(x, 2) for x in range(10)])
    container.floor_colors.update({piece: 'white' for piece in [(x, 1)
                                   for x in range(10)] + [(x, 2) for x in range(10)]})
    container.check_if_layer_filled()
    assert container.floor == [(x, 0) for x in range(10)] + [(x, 1) for x in range(10)]


def test_check_if_layer_not_filled():
    container = Container(10, 10)
    container.floor.extend([(x, 0) for x in range(5)])
    container.check_if_layer_filled()
    assert container.floor == [(x, 0) for x in range(10)] + [(x, 0) for x in range(5)]

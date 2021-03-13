import pytest

from block import BlockA, BlockB, BlockC, BlockD, BlockE, Direction, BlockF, BlockG


@pytest.mark.parametrize("block_class, direction, expected", (
        (BlockA, Direction.DOWN, [(10, 9), (8, 9), (9, 9), (11, 9)]),
        (BlockB, Direction.DOWN, [(10, 9), (11, 9), (10, 8), (11, 8)]),
        (BlockC, Direction.DOWN, [(10, 9), (9, 9), (11, 9), (10, 10)]),
        (BlockD, Direction.DOWN, [(10, 9), (9, 9), (10, 10), (11, 10)]),
        (BlockE, Direction.DOWN, [(10, 9), (9, 9), (9, 10), (11, 9)])
))
def test_move_block_down(block_class, direction, expected):
    block = block_class((10, 10), 20)
    block.move(direction.DOWN)
    assert expected == block.pieces


@pytest.mark.parametrize("block_class, rotation90, rotation180, rotation270, rotation360", (
        (BlockA, [(10, 10), (10, 12), (10, 11), (10, 9)],  [(10, 10), (12, 10), (9, 10), (11, 10)],
         [(10, 10), (10, 8), (10, 9), (10, 11)], [(10, 10), (8, 10), (9, 10), (11, 10)]),
        (BlockB, [(10, 10), (10, 9), (11, 9), (11, 10)],  [(10, 10), (10, 9), (11, 9), (11, 10)],
         [(10, 10), (10, 9), (11, 9), (11, 10)], [(10, 10), (10, 9), (11, 9), (11, 10)]),
        (BlockC, [(10, 10), (10, 11), (10, 9), (11, 10)],  [(10, 10), (9, 10), (11, 10), (10, 9)],
         [(10, 10), (10, 11), (10, 9), (9, 10)], [(10, 10), (9, 10), (11, 10), (10, 11)]),
        (BlockD, [(10, 10), (10, 11), (11, 10), (11, 9)],  [(10, 10), (10, 9), (11, 10), (9, 9)],
         [(10, 9), (10, 10), (9, 10), (9, 11)], [(10, 10), (9, 10), (10, 11), (11, 11)]),
        (BlockE, [(10, 9), (10, 10), (10, 11), (11, 11)],  [(9, 10), (10, 10), (11, 10), (11, 9)],
         [(10, 9), (10, 10), (10, 11), (9, 9)], [(10, 10), (9, 10), (9, 11), (11, 10)]),
        (BlockF, [(10, 9), (10, 10), (11, 10), (11, 11)],  [(9, 10), (10, 9), (10, 10), (11, 9)],
         [(9, 10), (10, 10), (10, 11), (9, 9)], [(10, 10), (9, 11), (10, 11), (11, 10)]),
        (BlockG, [(10, 9), (10, 10), (10, 11), (11, 9)],  [(9, 10), (10, 10), (11, 10), (9, 9)],
         [(10, 9), (10, 10), (10, 11), (9, 11)], [(10, 10), (9, 10), (11, 11), (11, 10)])
))
def test_rotation(block_class, rotation90, rotation180, rotation270, rotation360):
    block = block_class((10, 10), 20)
    block.rotate()
    assert set(rotation90) == set(block.pieces)
    block.rotate()
    assert set(rotation180) == set(block.pieces)
    block.rotate()
    assert set(rotation270) == set(block.pieces)
    block.rotate()
    assert set(rotation360) == set(block.pieces)


@pytest.mark.parametrize("block_class, floor, expected", (
        (BlockA, [(10, 9), (10, 8), (10, 7)], True),
        (BlockB, [(8, 7), (9, 7), (10, 7)], False),
        (BlockB, [(8, 11), (9, 11), (10, 11)], False)))
def test_check_if_floor(block_class, floor, expected):
    block = block_class((10, 10), 20)
    assert block.check_if_floor(floor) == expected


@pytest.mark.parametrize("block_class, floor, expected", (
        (BlockA, [(10, 9), (10, 8), (10, 7)], False),
        (BlockB, [(8, 7), (9, 7), (10, 7)], True)))
def test_if_can_rotate(block_class, floor, expected):
    block = block_class((10, 10), 20)
    assert block.check_if_can_rotate(floor) == expected

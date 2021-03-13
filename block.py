from enum import Enum
import random


class Direction(Enum):
    UP = (0, 1)
    DOWN = (0, -1)
    RIGHT = (1, 0)
    LEFT = (-1, 0)


def rotation(x, y, clock=True):
    if x < 0 and y < 0:
        new_x, new_y = x, -y
    elif x > 0 and y < 0:
        new_x, new_y = -x, y
    elif x < 0 and y > 0:
        new_x, new_y = -x, y
    elif x > 0 and y > 0:
        new_x, new_y = x, -y
    elif x == 0 and y < 0:
        new_x, new_y = y, x
    elif x == 0 and y > 0:
        new_x, new_y = y, x
    elif x < 0 and y == 0:
        new_x, new_y = y, -x
    elif x > 0 and y == 0:
        new_x, new_y = y, -x,
    else:
        new_x, new_y = x, y
    return (new_x, new_y) if clock else (-new_x, -new_y)


class Block:
    def __init__(self, center: tuple, x_max, color="white"):
        self.pieces = [center]
        self.center = center
        self.color = color
        self.in_air = True
        self.can_move_right = True
        self.can_move_left = True
        self.x_max = x_max

    def move(self, direction):
        if not self.in_air:
            return
        x, y = direction.value
        self.center = (self.center[0] + x, self.center[1] + y)
        for i, (px, py) in enumerate(self.pieces):
            px = (px + x)
            py = (py + y)
            self.pieces[i] = (px, py)
        for i, (px, py) in enumerate(self.next_rotation):
            px = (px + x)
            py = (py + y)
            self.next_rotation[i] = (px, py)
        self.can_move_left = True
        self.can_move_right = True

    def check_if_floor(self, surface):
        for (sx, sy) in surface:
            for (x, y) in self.pieces:
                if x == sx and y-1 == sy:
                    self.in_air = False
                if x + 1 == sx and y == sy or x + 1 == self.x_max:
                    self.can_move_right = False
                if x - 1 == sx and y == sy or x == 0:
                    self.can_move_left = False
        if not self.in_air:
            return True
        return False

    def check_next_rotation(self):
        self.next_rotation = []
        for x, y in self.pieces:
            x -= self.center[0]
            y -= self.center[1]
            new_x, new_y = rotation(x, y, clock=True)
            new_x += self.center[0]
            new_y += self.center[1]
            self.next_rotation.append((new_x, new_y))

    def rotate(self):
        self.pieces = self.next_rotation
        self.check_next_rotation()

    def check_if_can_rotate(self, surface):
        if not self.in_air:
            return False
        for (x, y) in self.next_rotation:
            if x <= 0 or x >= self.x_max:
                return False
        for (sx, sy) in surface:
            for (x, y) in self.pieces:
                if x == sx and y == sy:
                    return False
            for (x, y) in self.next_rotation:
                if x == sx and y == sy:
                    return False
        return True

    def __radd__(self, other):
        if isinstance(other, list):
            other.extend(self.pieces)
            return other
        else:
            raise NotImplemented

    def __repr__(self):
        return str(self.pieces)


class BlockA(Block):
    def __init__(self, center: tuple, x_max, color="white"):
        Block.__init__(self, center, x_max, color)
        x, y = center
        self.pieces = [center, (x-2, y), (x-1, y), (x+1, y)]
        self.in_air = True
        self.next_rotation = []
        self.check_next_rotation()


class BlockB(Block):
    def __init__(self, center: tuple, x_max, color="white"):
        Block.__init__(self, center, x_max, color)
        x, y = center
        self.pieces = [center, (x+1, y), (x, y-1), (x+1, y-1)]
        self.in_air = True
        self.next_rotation = []
        self.check_next_rotation()

    def check_next_rotation(self):
        self.next_rotation = self.pieces[:]


class BlockC(Block):
    def __init__(self, center: tuple, x_max, color="white"):
        Block.__init__(self, center, x_max, color)
        x, y = center
        self.pieces = [center, (x - 1, y), (x + 1, y), (x, y + 1)]
        self.in_air = True
        self.next_rotation = []
        self.check_next_rotation()


class BlockD(Block):
    def __init__(self, center: tuple, x_max, color="white"):
        Block.__init__(self, center, x_max, color)
        x, y = center
        self.pieces = [center, (x - 1, y), (x, y + 1), (x + 1, y + 1)]
        self.in_air = True
        self.next_rotation = []
        self.check_next_rotation()


class BlockE(Block):
    def __init__(self, center: tuple, x_max, color="white"):
        Block.__init__(self, center, x_max, color)
        x, y = center
        self.pieces = [center, (x - 1, y), (x - 1, y + 1), (x + 1, y)]
        self.in_air = True
        self.next_rotation = []
        self.check_next_rotation()


class BlockF(Block):
    def __init__(self, center: tuple, x_max, color="white"):
        Block.__init__(self, center, x_max, color)
        x, y = center
        self.pieces = [center, (x + 1, y), (x, y + 1), (x - 1, y + 1)]
        self.in_air = True
        self.next_rotation = []
        self.check_next_rotation()


class BlockG(Block):
    def __init__(self, center: tuple, x_max, color="white"):
        Block.__init__(self, center, x_max, color)
        x, y = center
        self.pieces = [center, (x + 1, y), (x - 1, y), (x + 1, y + 1)]
        self.in_air = True
        self.next_rotation = []
        self.check_next_rotation()


def random_block(xs, ys):
    block = random.choice(*[Block.__subclasses__()])
    color = random.choice(["red", "yellow", "blue", "green", "white", "purple"])
    return block((xs//2, ys - 2), xs, color=color)

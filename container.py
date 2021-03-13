import block


class Container:
    def __init__(self, xs, ys):
        self.xs = xs
        self.ys = ys
        self.floor = [(x, 0) for x in range(xs)]
        self.block = block.random_block(xs, ys)
        self.ceiling = ys - 2
        self.floor_colors = {piece: 'white' for piece in self.floor}

    def check_if_ceiling(self):
        for x, y in self.floor:
            if y >= self.ceiling:
                return True
        return False

    def check_if_block_on_floor(self):
        if self.block.check_if_floor(self.floor):
            self.floor += self.block
            for piece in self.block.pieces:
                self.floor_colors[piece] = self.block.color
            self.block = block.random_block(self.xs, self.ys)

    def check_if_layer_filled(self):
        layers = {layer: [x for x, y in self.floor if y == layer] for layer in {y for x, y in self.floor}
                  if layer != 0}
        for layer, pieces in layers.items():
            if len(pieces) == self.xs:
                self.delete_layer(layer)

    def delete_layer(self, layer):
        to_remove = []
        for i, piece in enumerate(self.floor):
            if piece[1] == layer:
                to_remove.append(piece)
            elif piece[1] > layer:
                self.floor[i] = (piece[0], piece[1]-1)
                self.floor_colors[(piece[0], piece[1]-1)] = self.floor_colors[piece]
        for piece in to_remove:
            self.floor.remove(piece)

    def move_block(self, direction):
        self.check_if_block_on_floor()
        if not self.block.can_move_left and direction == block.Direction.LEFT:
            return
        elif not self.block.can_move_right and direction == block.Direction.RIGHT:
            return
        self.block.move(direction)

    def rotate_block(self):
        if self.block.check_if_can_rotate(self.floor):
            self.block.rotate()

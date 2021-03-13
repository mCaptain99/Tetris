import random
import time

import pygame

from block import Direction
from container import Container

size_x = 15
size_y = 20
piece_size = 20
board_x = size_x * piece_size
board_y = size_y * piece_size

colors = {
    'red': pygame.image.load("img/red.png"),
    'blue': pygame.image.load("img/blue.png"),
    'green': pygame.image.load("img/green.png"),
    'yellow': pygame.image.load("img/yellow.png"),
    'purple': pygame.image.load("img/purple.png"),
    'white': pygame.image.load("img/white.png")
}


def blit_container(container, screen):
    screen.fill((0, 0, 0))
    for piece in container.floor:
        screen.blit(colors[container.floor_colors[piece]],
                    (piece_size * piece[0], board_y - piece_size * piece[1]))
    for piece in container.block.pieces:
        screen.blit(colors[container.block.color],
                    (piece_size * piece[0], board_y - piece_size * piece[1]))
    pygame.display.flip()


def end_game(screen, result):
    while True:
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
        text = font.render('''End of game. Your result is {}. 
                            Press any key to close'''.format(result), False, (255, 255, 255))
        screen.blit(text, (20, board_x // 2))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                else:
                    main()


def main():
    pygame.init()
    screen = pygame.display.set_mode((board_x, board_y))
    running = True
    container = Container(size_x, size_y)
    while running:
        blit_container(container, screen)
        for event in pygame.event.get():
            if event and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    container.rotate_block()
                elif event.key == pygame.K_DOWN:
                    container.move_block(Direction.DOWN)
                elif event.key == pygame.K_RIGHT:
                    container.move_block(Direction.RIGHT)
                elif event.key == pygame.K_LEFT:
                    container.move_block(Direction.LEFT)
                blit_container(container, screen)
        time.sleep(0.1)
        container.move_block(Direction.DOWN)
        blit_container(container, screen)
        time.sleep(0.1)
        container.check_if_layer_filled()
        time.sleep(0.1)
        blit_container(container, screen)
        if container.check_if_ceiling():
            end_game(screen, 0)


if __name__ == '__main__':
    main()

from classes import Game
import pygame, sys
from pygame.locals import *

# Vars
WHITE = (255, 255, 255)
LIGHT_SQUARE = (235, 235, 235)
DARK_SQUARE = (150, 150, 150)
SIZE = 60

# Object that controls the logic of the game
game = Game(10)

g_board = []
x, y = 0, 0
for i, row in enumerate(game.board):
    sqr = []
    for j, square in enumerate(row):
        sqr.append(pygame.Rect(x, y, SIZE, SIZE))
        x = sqr[j].right
    g_board.append(sqr)
    x = 0
    y = sqr[i].bottom


pygame.init()
display = pygame.display.set_mode((SIZE * game.board_size, SIZE * game.board_size))
pygame.display.set_caption("Game of the Amazons")

for i, row in enumerate(g_board):
    if i % 2 == 0:
        for j, square in enumerate(row):
            if j % 2 == 0:
                pygame.draw.rect(display, LIGHT_SQUARE, square)
            else:
                pygame.draw.rect(display, DARK_SQUARE, square)
    else:
        for j, square in enumerate(row):
            if j % 2 == 0:
                pygame.draw.rect(display, DARK_SQUARE, square)
            else:
                pygame.draw.rect(display, LIGHT_SQUARE, square)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.quit()
    pygame.display.update()
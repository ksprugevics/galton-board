import pygame

import colors


HEIGHT = 900
WIDTH  = 600

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))


def drawFrame():
    WINDOW.fill(colors.BACKGROUND)

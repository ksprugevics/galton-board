import pygame

import colors


HEIGHT = 900
WIDTH = 600

BEAD_RADIUS = 5


POLYGONS = []
BEADS = []
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))


def drawPolygons():
    for poly in POLYGONS:
        pygame.draw.polygon(WINDOW, poly[1], poly[0])


def drawBeads():
    for bead in BEADS:
        pygame.draw.circle(WINDOW, colors.BEAD,
                           bead.body.position, BEAD_RADIUS)


def drawFrame():
    WINDOW.fill(colors.BACKGROUND)
    drawPolygons()
    drawBeads()

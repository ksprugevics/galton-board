import pygame

import colors


HEIGHT = 900
WIDTH = 600

FUNNEL_HEIGHT = 100

BEAD_RADIUS = 5
PEG_RADIUS = 5
PEG_HEIGHT_MARGIN = 20
PEG_ROWS = 20


POLYGONS = []
BEADS = []
PEGS = []

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))


def drawPolygons():
    for poly in POLYGONS:
        pygame.draw.polygon(WINDOW, poly[1], poly[0])


def drawCircles(color, circleShapes):
    for c in circleShapes:
        pygame.draw.circle(WINDOW, color, c.body.position, c.radius)


def drawFrame():
    WINDOW.fill(colors.BACKGROUND)
    drawCircles(colors.WALL, PEGS)
    drawCircles(colors.BEAD, BEADS)
    drawPolygons()

import pygame, sys
from pygame.locals import *
import pymunk
import physics_objects
import drawing

BACKGROUND = (125, 125, 125)
WINDOW_HEIGHT = 900
WINDOW_WIDTH  = 900

OUTER_WALL_THICKNESS = 20
BEAD_RADIUS = 10


WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

SPACE = pymunk.Space()
SPACE.gravity = (0, 1)
SIMULATION_SPEED = 1/50

fun = physics_objects.createFunnel(SPACE, WINDOW_WIDTH, 440, 100, 100)
beads = [physics_objects.createBead(SPACE, (100, 50), BEAD_RADIUS), physics_objects.createBead(SPACE, (460, 50), BEAD_RADIUS)]
walls = physics_objects.createBorders(SPACE, WINDOW_WIDTH, WINDOW_HEIGHT, OUTER_WALL_THICKNESS)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    SPACE.step(SIMULATION_SPEED)

    WINDOW.fill(BACKGROUND)
    drawing.drawFunnel(WINDOW, fun)
    drawing.drawBorders(WINDOW, walls, OUTER_WALL_THICKNESS)
    drawing.drawBeads(WINDOW, beads)
    pygame.display.update()
    
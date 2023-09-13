import pygame, sys
from pygame.locals import *
import pymunk
import physics_objects
import drawing


WINDOW_HEIGHT = 900
WINDOW_WIDTH  = 900

OUTER_WALL_THICKNESS = 20
BEAD_RADIUS = 10
BEAD_COUNT = 100
PEG_RADIUS = 4
PEG_ROW_MARGIN = 50
ROW_COUNT = 6


WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

SPACE = pymunk.Space()
SPACE.gravity = (0, 1)
SIMULATION_SPEED = 0.1

fun = physics_objects.createFunnel(SPACE, WINDOW_WIDTH, 440, 160, 120)
beads = physics_objects.spawnBeads(SPACE, BEAD_COUNT, BEAD_RADIUS, WINDOW_WIDTH / 2, 100)
walls = physics_objects.createBorders(SPACE, WINDOW_WIDTH, WINDOW_HEIGHT, OUTER_WALL_THICKNESS)
pegs, pegCenters = physics_objects.createPegs(SPACE, ROW_COUNT, 350, WINDOW_WIDTH, PEG_RADIUS)
slots = physics_objects.createSlots(SPACE, PEG_RADIUS * 2, 100, pegCenters)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    SPACE.step(SIMULATION_SPEED)

    WINDOW.fill(drawing.colors.BACKGROUND)
    drawing.drawFunnel(WINDOW, fun)
    drawing.drawCircles(WINDOW, pegs, drawing.colors.PEG)
    drawing.drawSlots(WINDOW, slots)
    drawing.drawBorders(WINDOW, walls, OUTER_WALL_THICKNESS)
    drawing.drawCircles(WINDOW, beads, drawing.colors.BEAD)
    pygame.display.update()
    
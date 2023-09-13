import pygame, sys
from pygame.locals import *
import pymunk
import physics_objects
import drawing


WINDOW_HEIGHT = 900
WINDOW_WIDTH  = 500
OUTER_WALL_THICKNESS = 20

BEAD_RADIUS = 10
BEAD_COUNT = 1
PEG_RADIUS = 10

PEG_ROW_MARGIN = 50
PEG_ROW_COUNT = 6

SIMULATION_SPEED = 1 / 50


WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

SPACE = pymunk.Space()
handler = SPACE.add_collision_handler(physics_objects.BEAD_COLLISION_TYPE, physics_objects.PEG_COLLISION_TYPE)
handler.pre_solve = physics_objects.pegBounceCallback
SPACE.gravity = (0, 1)

beads = physics_objects.spawnBeads(SPACE, BEAD_COUNT, BEAD_RADIUS, WINDOW_WIDTH / 2, 100)
pegs, pegCenters = physics_objects.createPegs(SPACE, PEG_ROW_COUNT, 350, WINDOW_WIDTH, PEG_RADIUS)
slots = physics_objects.createSlots(SPACE, PEG_RADIUS * 2, 100, pegCenters)
borders = physics_objects.createBorders(SPACE, WINDOW_WIDTH, WINDOW_HEIGHT, 25)
funnel = physics_objects.createFunnel(SPACE, WINDOW_WIDTH, BEAD_RADIUS)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    SPACE.step(SIMULATION_SPEED)

    WINDOW.fill(drawing.colors.BACKGROUND)
    drawing.drawCircles(WINDOW, pegs, drawing.colors.PEG)
    drawing.drawSlots(WINDOW, slots)
    for w in borders:
        drawing.drawRectangle(WINDOW, drawing.colors.WALL, w)
    for f in funnel:
        drawing.drawPoly(WINDOW, drawing.colors.WALL, f)
    drawing.drawCircles(WINDOW, beads, drawing.colors.BEAD)
    pygame.display.update()
    
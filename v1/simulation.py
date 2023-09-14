import pygame, sys
from pygame.locals import *
import pymunk
import physics_objects
import drawing


WINDOW_HEIGHT = 900
WINDOW_WIDTH  = 900
OUTER_WALL_THICKNESS = 20

BEAD_RADIUS = 5
BEAD_COUNT = 100
PEG_RADIUS = 5

PEG_ROW_MARGIN = 200
PEG_ROW_COUNT = 15

SIMULATION_SPEED = 1 / 5

currentBeadCount = 1
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

SPACE = pymunk.Space()
handler = SPACE.add_collision_handler(physics_objects.BEAD_COLLISION_TYPE, physics_objects.PEG_COLLISION_TYPE)
handler.pre_solve = physics_objects.pegBounceCallback
SPACE.gravity = (0, 1)

beads = [physics_objects.createBead(SPACE, (WINDOW_WIDTH / 2, 100), BEAD_RADIUS)]
pegs, pegCenters, wings, slots = physics_objects.createPegs(SPACE, PEG_ROW_COUNT, 350, WINDOW_WIDTH, PEG_RADIUS)
borders = physics_objects.createBorders(SPACE, WINDOW_WIDTH, WINDOW_HEIGHT, 25)
funnel = physics_objects.createFunnel(SPACE, WINDOW_WIDTH, BEAD_RADIUS)

checkpoint = pygame.time.get_ticks()
pygame.init()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    SPACE.step(SIMULATION_SPEED)
    now = pygame.time.get_ticks()
    if now - checkpoint > 750 and currentBeadCount < BEAD_COUNT:
        currentBeadCount += 1
        checkpoint = now
        beads.append(physics_objects.createBead(SPACE, (WINDOW_WIDTH / 2, 100), BEAD_RADIUS))


    WINDOW.fill(drawing.colors.BACKGROUND)
    drawing.drawCircles(WINDOW, pegs, drawing.colors.PEG)
    drawing.drawSlots(WINDOW, slots)
    for w in borders:
        drawing.drawRectangle(WINDOW, drawing.colors.WALL, w)
    for f in funnel:
        drawing.drawPoly(WINDOW, drawing.colors.WALL, f)
    drawing.drawCircles(WINDOW, beads, drawing.colors.BEAD)
    for w in wings:
        drawing.drawPoly(WINDOW, drawing.colors.WALL, w)
    pygame.display.update()
    
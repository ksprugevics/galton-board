import pygame, sys
from pygame.locals import *
import pymunk
import physics_objects
import drawing

BACKGROUND = (125, 125, 125)
WINDOW_HEIGHT = 500
WINDOW_WIDTH  = 500

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

SPACE = pymunk.Space()
SPACE.gravity = (0, 1)
SIMULATION_SPEED = 1/50

fun = physics_objects.createFunnel(SPACE)
beads = [physics_objects.createBead(SPACE, (10, 50)), physics_objects.createBead(SPACE, (460, 50))]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    SPACE.step(SIMULATION_SPEED)

    WINDOW.fill(BACKGROUND)
    drawing.drawFunnel(WINDOW, fun)
    drawing.drawBeads(WINDOW, beads)
    pygame.display.update()
    
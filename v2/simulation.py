import sys
import pygame
import pygame.locals

import drawing
import physics


SIMULATION_SPEED = 1 / 50


borders = physics.createBorders()
drawing.POLYGONS.extend(borders)

bead = physics.createBead()
drawing.BEADS.append(bead)


pygame.init()
while True:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()

    physics.SPACE.step(SIMULATION_SPEED)
    drawing.drawFrame()
    pygame.display.update()

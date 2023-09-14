import sys
import pygame
import pygame.locals

import drawing
import physics


SIMULATION_SPEED = 1 / 5
BEAD_SPAWN_RATE = 300
MAX_BEAD_COUNT = 110

pygame.display.set_caption("Galton board")

borders = physics.createBorders()
drawing.POLYGONS.extend(borders)

bead = physics.createBead()
drawing.BEADS.append(bead)

pegs, wings, slots = physics.createPegs()
drawing.PEGS.extend(pegs)
drawing.POLYGONS.extend(wings)
drawing.POLYGONS.extend(slots)

checkpointTick = 0
beadCount = 1


pygame.init()
while True:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()

    currentTick = pygame.time.get_ticks()
    if currentTick - checkpointTick > BEAD_SPAWN_RATE and beadCount < MAX_BEAD_COUNT:
        beadCount += 1
        checkpointTick = currentTick
        bead = physics.createBead()
        drawing.BEADS.append(bead)

    physics.SPACE.step(SIMULATION_SPEED)
    drawing.drawFrame()
    pygame.display.update()

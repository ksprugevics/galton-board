import sys
import pygame
import pygame.locals

import drawing

while True:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()

    drawing.drawFrame()
    pygame.display.update()
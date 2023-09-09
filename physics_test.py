import pygame, sys
from pygame.locals import *
import pymunk


BACKGROUND = (125, 125, 125)
WINDOW_HEIGHT = 500
WINDOW_WIDTH  = 500

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def bead(space, pos):
    rad = 20
    body = pymunk.Body(1, 30, pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, rad)
    space.add(body, shape)
    return shape

def staticBead(space, pos):
    body = pymunk.Body(1, 0, pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, 20)
    space.add(body, shape)
    return shape

def walls(space):
    body1 = pymunk.Body(1, 30, pymunk.Body.STATIC)
    body1.position = 0, WINDOW_HEIGHT - 30 
    shape = pymunk.Segment(body1, (0, 0), (WINDOW_WIDTH, 0), 0)
    space.add(body1, shape)
    return shape

def drawBeads(beads): 
    for bead in beads:
        pygame.draw.circle(WINDOW, (255, 255, 0), bead.body.position, 20)

def drawFloor(wall):
    rect = pygame.Rect(wall.bb.left, wall.bb.top, wall.bb.right, wall.bb.top)
    pygame.draw.rect(WINDOW, (0, 0, 0), rect)


space = pymunk.Space()
space.gravity = (0, 1)

beads = []
beads.append(bead(space, (100, 100)))
staticBeads = []
staticBeads.append(staticBead(space, (104, 200)))
bottomWall = walls(space)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    WINDOW.fill(BACKGROUND)

    space.step(1/50)
    drawBeads(beads)
    drawBeads(staticBeads)
    drawFloor(bottomWall)

    pygame.display.update()

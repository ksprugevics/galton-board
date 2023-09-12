import pygame


def drawFunnel(WINDOW, funnel):
    pygame.draw.line(WINDOW, (0, 0, 0), (funnel[0].bb.right, funnel[0].bb.top), (funnel[0].bb.left, funnel[0].bb.bottom), 5)
    pygame.draw.line(WINDOW, (0, 0, 0), (funnel[1].bb.left, funnel[1].bb.top), (funnel[1].bb.right, funnel[1].bb.bottom), 5)


def drawBeads(WINDOW,  beads): 
    for bead in beads:
        pygame.draw.circle(WINDOW, (255, 255, 0), bead.body.position, bead.radius)


def drawBorders(WINDOW, walls, thickness):
    pygame.draw.line(WINDOW, (255, 255, 255), (walls[0].bb.left, walls[0].bb.bottom + thickness / 2), (walls[0].bb.right, walls[0].bb.top + thickness / 2), thickness)
    pygame.draw.line(WINDOW, (255, 255, 255), (walls[1].bb.left - thickness / 2, walls[1].bb.bottom), (walls[1].bb.right - thickness / 2, walls[1].bb.top), thickness)
    pygame.draw.line(WINDOW, (255, 255, 255), (walls[2].bb.left + thickness / 2, walls[2].bb.bottom), (walls[2].bb.right + thickness / 2, walls[2].bb.top), thickness)

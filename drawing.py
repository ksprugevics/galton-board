import pygame


def drawFunnel(WINDOW, funnel):
    print(funnel[1].bb)
    pygame.draw.line(WINDOW, (0, 0, 0), (funnel[0].bb.right, funnel[0].bb.top), (funnel[0].bb.left, funnel[0].bb.bottom), 5)
    pygame.draw.line(WINDOW, (0, 0, 0), (funnel[1].bb.left, funnel[1].bb.top), (funnel[1].bb.right, funnel[1].bb.bottom), 5)



def drawBeads(WINDOW,  beads): 
    for bead in beads:
        # print(bead.body.position)
        pygame.draw.circle(WINDOW, (255, 255, 0), bead.body.position, 20)

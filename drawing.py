import pygame
import colors


def drawFunnel(WINDOW, funnel):
    pygame.draw.line(WINDOW, colors.WALL, (funnel[0].bb.right, funnel[0].bb.top), (funnel[0].bb.left, funnel[0].bb.bottom), 5)
    pygame.draw.line(WINDOW, colors.WALL, (funnel[1].bb.left, funnel[1].bb.top), (funnel[1].bb.right, funnel[1].bb.bottom), 5)


def drawCircles(WINDOW, pegs, color):
    for peg in pegs:
        pygame.draw.circle(WINDOW, color, peg.body.position, peg.radius)


def drawBorders(WINDOW, walls, thickness):
    pygame.draw.line(WINDOW, colors.WALL, (walls[0].bb.left, walls[0].bb.bottom + thickness / 2), (walls[0].bb.right, walls[0].bb.top + thickness / 2), thickness)
    pygame.draw.line(WINDOW, colors.WALL, (walls[1].bb.left - thickness / 2, walls[1].bb.bottom), (walls[1].bb.right - thickness / 2, walls[1].bb.top), thickness)
    pygame.draw.line(WINDOW, colors.WALL, (walls[2].bb.left + thickness / 2, walls[2].bb.bottom), (walls[2].bb.right + thickness / 2, walls[2].bb.top), thickness)


def drawSlots(WINDOW, slots):
    for slot in slots:
        slot = pygame.Rect(slot[0][0], slot[0][1], slot[2][0] - slot[0][0], 200)
        pygame.draw.rect(WINDOW, colors.PEG, slot)


def drawRectangle(WINDOW, color, bounds):
    rect = pygame.Rect(bounds[0][0], bounds[0][1], bounds[2][0] - bounds[0][0], bounds[2][1] - bounds[0][1])
    pygame.draw.rect(WINDOW, color, rect)

def drawPoly(WINDOW, color, coords):
    pygame.draw.polygon(WINDOW, color, coords)
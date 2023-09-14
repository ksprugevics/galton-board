import pymunk

from drawing import WIDTH, HEIGHT, colors, BEAD_RADIUS


BEAD_COLLISION_TYPE = 1
PEG_COLLISION_TYPE = 2

SPACE = pymunk.Space()
SPACE.gravity = (0, 1)


def createBorders():
    botWallWidth = 25
    sideWallWidth = WIDTH / 2 - BEAD_RADIUS
    sideWallHeight = HEIGHT / 2

    botCoords = [(0, HEIGHT - botWallWidth),
                 (WIDTH, HEIGHT - botWallWidth),
                 (WIDTH, HEIGHT),
                 (0, HEIGHT)]

    leftWallCoords = [(0, 0),
                      (sideWallWidth, 0),
                      (sideWallWidth, sideWallHeight),
                      (0, sideWallHeight)]

    rightWallCoords = [(WIDTH / 2 + BEAD_RADIUS, 0),
                       (WIDTH, 0),
                       (WIDTH, sideWallHeight),
                       (WIDTH / 2 + BEAD_RADIUS, sideWallHeight)]

    botWall = pymunk.Poly(SPACE.static_body, botCoords)
    leftWall = pymunk.Poly(SPACE.static_body, leftWallCoords)
    rightWall = pymunk.Poly(SPACE.static_body, rightWallCoords)
    SPACE.add(botWall, leftWall, rightWall)
    return [(botCoords, colors.WALL), (leftWallCoords, colors.WALL), (rightWallCoords, colors.WALL)]


def createBead():
    body = pymunk.Body(10, 30, pymunk.Body.DYNAMIC)
    body.position = WIDTH / 2, 10
    shape = pymunk.Circle(body, BEAD_RADIUS)

    shape.elasticity = 0
    shape.collision_type = BEAD_COLLISION_TYPE
    SPACE.add(body, shape)
    return shape

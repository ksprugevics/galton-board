import pymunk
import random

from drawing import *


BEAD_COLLISION_TYPE = 1
PEG_COLLISION_TYPE = 2

SPACE = pymunk.Space()
SPACE.gravity = (0, 1)


def createBorders():
    botWallWidth = 25
    sideWallWidth = WIDTH / 2 - BEAD_RADIUS
    sideWallHeight = FUNNEL_HEIGHT

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


def createPegs():
    pegs = []
    wings = []

    startHeight = FUNNEL_HEIGHT + BEAD_RADIUS * 3
    xMid = WIDTH / 2

    for row in range(PEG_ROWS):
        pegCenters = []
        pegCountInRow = row + 1
        pegCountOnEachSide = -(-pegCountInRow // 2)
        offSet = 0

        leftMostPeg = None
        rightMostPeg = None

        if pegCountInRow % 2 != 0:
            middlePeg = pymunk.Body(0, 0, pymunk.Body.STATIC)
            middlePeg.position = xMid, startHeight + row * PEG_HEIGHT_MARGIN
            middlePegShape = pymunk.Circle(middlePeg, PEG_RADIUS)
            middlePegShape.collision_type = PEG_COLLISION_TYPE
            SPACE.add(middlePeg, middlePegShape)
            pegs.append(middlePegShape)
        else:
            offSet = PEG_RADIUS * 2

        for i in range(0, pegCountOnEachSide):
            pegRight = pymunk.Body(0, 0, pymunk.Body.STATIC)
            pegRight.position = xMid + offSet + i * (PEG_RADIUS * 4), startHeight + row * PEG_HEIGHT_MARGIN
            pegRightShape = pymunk.Circle(pegRight, PEG_RADIUS)
            pegRightShape.collision_type = PEG_COLLISION_TYPE

            pegLeft = pymunk.Body(0, 0, pymunk.Body.STATIC)
            pegLeft.position = xMid - offSet - i * (PEG_RADIUS * 4), startHeight + row * PEG_HEIGHT_MARGIN
            pegLeftShape = pymunk.Circle(pegLeft, PEG_RADIUS)
            pegLeftShape.collision_type = PEG_COLLISION_TYPE

            if i == pegCountOnEachSide - 1:
                rightMostPeg = pegRight
            leftMostPeg = pegLeft

            pegs += [pegLeftShape, pegRightShape]
            pegCenters += [pegRight.position, pegLeft.position]
            SPACE.add(pegLeft, pegLeftShape, pegRight, pegRightShape)

        wings.append(createWing(leftMostPeg.position.x, leftMostPeg.position.y, True))
        wings.append(createWing(rightMostPeg.position.x, rightMostPeg.position.y, False))
    slots = createSlots(pegCenters, leftMostPeg, rightMostPeg)
    return pegs, wings, slots


def createWing(x, y, left):
    if left:
        coords = [(x - PEG_RADIUS * 3, y + PEG_RADIUS), (0, y + PEG_RADIUS), (0, y - 100), (x - PEG_RADIUS * 3, y - 100)]
    else:
        coords = [(x + PEG_RADIUS * 3, y + PEG_RADIUS), (WIDTH, y + PEG_RADIUS), (WIDTH, y - 100), (x + PEG_RADIUS * 3, y - 100)]

    SPACE.add(pymunk.Poly(SPACE.static_body, coords))
    return (coords, colors.WALL)


def createSlots(pegs, leftMostPeg, rightMostPeg):
    slotWidth = PEG_RADIUS * 2
    slots = []
    leftMostSlotCoords = [
        (leftMostPeg.position.x - WIDTH, leftMostPeg.position.y ),
        (leftMostPeg.position.x - slotWidth * 1.5, leftMostPeg.position.y),
        (leftMostPeg.position.x - slotWidth * 1.5, leftMostPeg.position.y + HEIGHT),
        (leftMostPeg.position.x - WIDTH, leftMostPeg.position.y + HEIGHT)
    ]

    rightMostSlotCoords = [
        (rightMostPeg.position.x + slotWidth * 1.5, rightMostPeg.position.y),
        (rightMostPeg.position.x + WIDTH, rightMostPeg.position.y),
        (rightMostPeg.position.x + WIDTH, rightMostPeg.position.y + HEIGHT),
        (rightMostPeg.position.x + slotWidth * 1.5, rightMostPeg.position.y + HEIGHT)
    ]

    slots.append((leftMostSlotCoords, colors.WALL))
    slots.append((rightMostSlotCoords, colors.WALL))
    leftMostSlot = pymunk.Poly(SPACE.static_body, leftMostSlotCoords)
    rightMostSlot = pymunk.Poly(SPACE.static_body, rightMostSlotCoords)
    SPACE.add(leftMostSlot, rightMostSlot)

    for peg in pegs:
        slotCoords = [
            (peg.x - slotWidth / 2, peg.y),
            (peg.x + slotWidth / 2, peg.y),
            (peg.x + slotWidth / 2, peg.y + 1000),
            (peg.x - slotWidth / 2, peg.y + 1000)
        ]
        slots.append((slotCoords, colors.WALL))
        slot = pymunk.Poly(SPACE.static_body, slotCoords)
        SPACE.add(slot)
    
    return slots


def pegBounceCallback(arbiter, space, data):
    bead_shape, peg_shape = arbiter.shapes
    # Randomly decide the direction of the bounce
    if random.random() < 0.5:
        impulse = (-0.5, 0.0)
    else:
         impulse = (0.5, 0.0)
    bead_shape.body.apply_impulse_at_local_point(impulse)
    return True


handler = SPACE.add_collision_handler(BEAD_COLLISION_TYPE, PEG_COLLISION_TYPE)
handler.pre_solve = pegBounceCallback

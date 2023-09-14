import pymunk
import random


BEAD_COLLISION_TYPE = 1
PEG_COLLISION_TYPE = 2


def createBorders(space, WINDOW_WIDTH, WINDOW_HEIGHT, wallWidth):
    topCoords = [(0, 0), (WINDOW_WIDTH, 0), (WINDOW_WIDTH, wallWidth), (0, wallWidth)]
    botCoords = [(0, WINDOW_HEIGHT - wallWidth), (WINDOW_WIDTH, WINDOW_HEIGHT - wallWidth), (WINDOW_WIDTH, WINDOW_HEIGHT), (0, WINDOW_HEIGHT)]
    leftCoords = [(0, 0), (wallWidth, 0), (wallWidth, WINDOW_HEIGHT), (0, WINDOW_HEIGHT)]
    rightCoords = [(WINDOW_WIDTH - wallWidth, 0), (WINDOW_WIDTH, 0), (WINDOW_WIDTH, WINDOW_HEIGHT), (WINDOW_WIDTH - wallWidth, WINDOW_HEIGHT)]
    top = pymunk.Poly(space.static_body, topCoords)
    bot = pymunk.Poly(space.static_body, botCoords)
    left = pymunk.Poly(space.static_body, leftCoords)
    right = pymunk.Poly(space.static_body, rightCoords)
    space.add(top, bot, left, right)
    return [topCoords, botCoords, leftCoords, rightCoords]


def createFunnel(space, WINDOW_WIDTH, beadRadius):
    xMid = WINDOW_WIDTH / 2
    yStart = 50
    yEnd = 300
    leftPolyCoords = [(0, yEnd), (xMid - beadRadius, yEnd), (xMid - beadRadius, yEnd - beadRadius), (0, yStart)]
    leftPoly = pymunk.Poly(space.static_body, leftPolyCoords)

    rightPolyCoords = [(WINDOW_WIDTH, yEnd), (xMid + beadRadius, yEnd), (xMid + beadRadius, yEnd - beadRadius), (WINDOW_WIDTH, yStart)]
    rightPoly = pymunk.Poly(space.static_body, rightPolyCoords)
    space.add(leftPoly, rightPoly)
    return [leftPolyCoords, rightPolyCoords]


def createBead(space, pos, rad):
    body = pymunk.Body(10, 30, pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, rad)

    shape.elasticity = 0
    shape.collision_type = BEAD_COLLISION_TYPE
    space.add(body, shape)
    return shape


def createLeftWing(space, x, y, pegRadius, WINDOW_WIDTH):
    rightCoords = [(x - pegRadius * 3, y + pegRadius), (0, y + pegRadius), (0, y - 100), (x - pegRadius * 3, y - 100)]
    right = pymunk.Poly(space.static_body, rightCoords)
    space.add(right)
    return rightCoords


def createRightWing(space, x, y, pegRadius, WINDOW_WIDTH):
    rightCoords = [(x + pegRadius * 3, y + pegRadius), (WINDOW_WIDTH, y + pegRadius), (WINDOW_WIDTH, y - 100), (x + pegRadius * 3, y - 100)]
    right = pymunk.Poly(space.static_body, rightCoords)
    space.add(right)
    return rightCoords


def createSlots(space, width, height, pegs, leftMostPeg, rightMostPeg):
    slots = []
    
    p0 = (leftMostPeg[0] - 1000, leftMostPeg[1] + 100 - height)
    p1 = (leftMostPeg[0] - width * 1.5, leftMostPeg[1] + 100 - height)
    p2 = (leftMostPeg[0] - width * 1.5, leftMostPeg[1] + 1000)
    p3 = (leftMostPeg[0] - 1000, leftMostPeg[1] + 1000)
    slot0 = [p0, p1, p2, p3]
    slots.append(slot0)
    slot = pymunk.Poly(space.static_body, slot0)
    space.add(slot)

    p0 = (rightMostPeg[0] + width * 1.5, rightMostPeg[1] + 100 - height)
    p1 = (rightMostPeg[0] + 1000, rightMostPeg[1] + 100 - height)
    p2 = (rightMostPeg[0] + 1000, rightMostPeg[1] + 1000)
    p3 = (rightMostPeg[0] + width * 1.5, rightMostPeg[1] + 1000)
    slot0 = [p0, p1, p2, p3]
    print(slot0)
    slots.append(slot0)
    slot = pymunk.Poly(space.static_body, slot0)
    space.add(slot)

         
    for peg in pegs:
        p0 = (peg.x - width / 2, peg.y + 100 - height)
        p1 = (peg.x + width / 2, peg.y + 100 - height)
        p2 = (peg.x + width / 2, peg.y + 1000)
        p3 = (peg.x - width / 2, peg.y + 1000)
        rect = [p0, p1, p2, p3]
        slots.append(rect)
        slot = pymunk.Poly(space.static_body, rect)
        space.add(slot)
    return slots


def createPegs(space, rows, startHeight, WINDOW_WIDTH, pegRadius):
    pegs = []
    wings = []
    xMid = WINDOW_WIDTH / 2
    rowMargin = 20
    for row in range(rows):
        pegCenters = []
        pegCountInRow = row + 1
        pegCountOnEachSide = -(-pegCountInRow // 2)
        offSet = 0
        rightMostPeg = None
        
        if pegCountInRow % 2 != 0:
            middlePeg = pymunk.Body(0, 0, pymunk.Body.STATIC)
            middlePeg.position = xMid, startHeight + row * rowMargin
            middlePegShape = pymunk.Circle(middlePeg, pegRadius)
            middlePegShape.collision_type = PEG_COLLISION_TYPE
            space.add(middlePeg, middlePegShape)
            pegs.append(middlePegShape)
        else:
            offSet = pegRadius * 2

        for i in range(0, pegCountOnEachSide):
            pegLeft = pymunk.Body(0, 0, pymunk.Body.STATIC)
            pegLeft.position = xMid + offSet + i * (pegRadius * 4), startHeight + row * rowMargin
            pegLeftShape = pymunk.Circle(pegLeft, pegRadius)
            pegLeftShape.collision_type = PEG_COLLISION_TYPE


            pegRight = pymunk.Body(0, 0, pymunk.Body.STATIC)
            pegRight.position = xMid - offSet - i * (pegRadius * 4), startHeight + row * rowMargin
            pegRightShape = pymunk.Circle(pegRight, pegRadius)
            pegRightShape.collision_type = PEG_COLLISION_TYPE

            if i == pegCountOnEachSide - 1:
                rightMostPeg = pegLeft

            pegs += [pegLeftShape, pegRightShape]
            pegCenters += [pegRight.position, pegLeft.position]
            space.add(pegLeft, pegLeftShape, pegRight, pegRightShape)

        leftMostPeg = (pegRight.position.x, pegRight.position.y)
        rightMostPeg = (rightMostPeg.position.x, rightMostPeg.position.y)
        wings.append(createLeftWing(space, leftMostPeg[0], leftMostPeg[1], pegRadius, WINDOW_WIDTH))
        wings.append(createRightWing(space, rightMostPeg[0], rightMostPeg[1], pegRadius, WINDOW_WIDTH))
    slots = createSlots(space, pegRadius * 2, 100, pegCenters, leftMostPeg, rightMostPeg)

    return pegs, pegCenters, wings, slots


def pegBounceCallback(arbiter, space, data):
    bead_shape, peg_shape = arbiter.shapes
    # Randomly decide the direction of the bounce
    if random.random() < 0.5:
        # Bounce to the left
        impulse = (-0.5, 0.0)
    else:
        # Bounce to the right
         impulse = (0.5, 0.0)
    bead_shape.body.apply_impulse_at_local_point(impulse)
    return True

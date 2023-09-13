import pymunk


def createFunnel(space, WINDOW_WIDTH, funnelWidth, funnelHeight, yPos):
    leftBody = pymunk.Body(None, None, pymunk.Body.STATIC)
    leftBody.position = 0, yPos # shape coordinates originate from here
    leftShape = pymunk.Segment(leftBody, (0, 0), (funnelWidth, funnelHeight), 0) # body coordinates + whatever
    rightBody = pymunk.Body(None, None, pymunk.Body.STATIC)
    rightBody.position = WINDOW_WIDTH - funnelWidth, yPos
    rightShape = pymunk.Segment(rightBody, (0, funnelHeight), (funnelWidth, 0), 0)

    space.add(leftBody, leftShape, rightBody, rightShape)
    return [leftShape, rightShape]


def createBead(space, pos, rad):
    body = pymunk.Body(1, 30, pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, rad)
    shape.elasticity = 0
    space.add(body, shape)
    return shape


def createBorders(space, WINDOW_WIDTH, WINDOW_HEIGHT, wallWidth):
    floor = pymunk.Body(0, 0, pymunk.Body.STATIC)
    floor.position = 0, WINDOW_HEIGHT - wallWidth 
    floorShape = pymunk.Segment(floor, (0, 0), (WINDOW_WIDTH, 0), 0)
    leftWall = pymunk.Body(0, 0, pymunk.Body.STATIC)
    leftWall.position = 0, 0 
    leftWallShape = pymunk.Segment(leftWall, (wallWidth, 0), (wallWidth, WINDOW_HEIGHT), 0)
    rightWall = pymunk.Body(0, 0, pymunk.Body.STATIC)
    rightWall.position = WINDOW_WIDTH - wallWidth, 0 
    rightWallShape = pymunk.Segment(rightWall, (0, 0), (0, WINDOW_HEIGHT), 0)

    space.add(floor, floorShape, leftWall, leftWallShape, rightWall, rightWallShape)
    return [floorShape, leftWallShape, rightWallShape]


def createSlots(space, WINDOW_WIDTH, WINDOW_HEIGHT, width, height, count):
    slots = []
    p0 = (WINDOW_WIDTH / 2 - width / 2, WINDOW_HEIGHT - height)
    p1 = (WINDOW_WIDTH / 2 + width / 2, WINDOW_HEIGHT - height)
    p2 = (WINDOW_WIDTH / 2 + width / 2, WINDOW_HEIGHT)
    p3 = (WINDOW_WIDTH / 2 - width / 2, WINDOW_HEIGHT)
    rect = [p0, p1, p2, p3]
    slots.append(rect)
    slot = pymunk.Poly(space.static_body, rect)
    space.add(slot)
    return slots


def createSlotsNew(space, width, height, pegs):
    slots = []
    for peg in pegs:
        p0 = (peg.x - width / 2, peg.y + 100 - height)
        p1 = (peg.x + width / 2, peg.y + 100 - height)
        p2 = (peg.x + width / 2, peg.y + 100)
        p3 = (peg.x - width / 2, peg.y + 100)
        rect = [p0, p1, p2, p3]
        slots.append(rect)
        slot = pymunk.Poly(space.static_body, rect)
        space.add(slot)
    return slots


def spawnBeads(space, count, rad, x, y):
    beads = []
    for _ in range(count):
        beads.append(createBead(space, (x, y), rad))
    return beads
        

def createPegs(space, rows, startHeight, WINDOW_WIDTH, pegRadius):
    pegs = []
    xMid = WINDOW_WIDTH / 2
    rowMargin = 70
    for row in range(rows):
        pegCenters = []
        pegCountInRow = row + 1
        pegCountInEachSide = -(-pegCountInRow // 2)
        offSet = 0

        if pegCountInRow % 2 != 0:
            middlePeg = pymunk.Body(0, 0, pymunk.Body.STATIC)
            middlePeg.position = xMid, startHeight + row * rowMargin
            middlePegShape = pymunk.Circle(middlePeg, pegRadius)
            space.add(middlePeg, middlePegShape)
            pegs.append(middlePegShape)
        else:
            offSet = rowMargin / 2

        for i in range(0, pegCountInEachSide):
            pegLeft = pymunk.Body(0, 0, pymunk.Body.STATIC)
            pegLeft.position = xMid + offSet + i * rowMargin, startHeight + row * rowMargin
            pegLeftShape = pymunk.Circle(pegLeft, pegRadius)
            pegRight = pymunk.Body(0, 0, pymunk.Body.STATIC)
            pegRight.position = xMid - offSet - i * rowMargin, startHeight + row * rowMargin
            pegRightShape = pymunk.Circle(pegRight, pegRadius)
            pegs += [pegLeftShape, pegRightShape]
            pegCenters += [pegRight.position, pegLeft.position]
            space.add(pegLeft, pegLeftShape, pegRight, pegRightShape)

    return pegs, pegCenters


import pymunk


def createFunnel(space, WINDOW_WIDTH, funnelWidth, funnelHeight, yPos):
    leftBody = pymunk.Body(None, None, pymunk.Body.STATIC)
    leftBody.position = 0, yPos # shape coordinates originate from here
    leftShape = pymunk.Segment(leftBody, (0, 0), (funnelWidth, funnelHeight), 0) # body coordinates + whatever
    rightBody = pymunk.Body(None, None, pymunk.Body.STATIC)
    rightBody.position = WINDOW_WIDTH - funnelWidth, yPos
    rightShape = pymunk.Segment(rightBody, (0, funnelHeight), (funnelWidth, 0), 0)

    space.add(leftBody, leftShape)
    space.add(rightBody, rightShape)
    return [leftShape, rightShape]


def createBead(space, pos, rad):
    body = pymunk.Body(1, 30, pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, rad)
    shape.elasticity = 1
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

    space.add(floor, floorShape)
    space.add(leftWall, leftWallShape)
    space.add(rightWall, rightWallShape)
    return [floorShape, leftWallShape, rightWallShape]


# def createPegs(space, rows, startHeight):
#     pass

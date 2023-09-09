import pymunk


def createFunnel(space):
    leftBody = pymunk.Body(None, None, pymunk.Body.STATIC)
    leftBody.position = 0, 100 # shape coordinates originate from here
    leftShape = pymunk.Segment(leftBody, (0, 0), (200, 50), 0) # body coordinates + whatever
    rightBody = pymunk.Body(None, None, pymunk.Body.STATIC)
    rightBody.position = 300, 100
    rightShape = pymunk.Segment(rightBody, (0, 50), (200, 0), 0)

    space.add(leftBody, leftShape)
    space.add(rightBody, rightShape)
    return [leftShape, rightShape]


def createBead(space, pos):
    rad = 20
    body = pymunk.Body(1, 30, pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, rad)
    space.add(body, shape)
    return shape
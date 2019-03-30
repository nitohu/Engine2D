import math

from Engine2D.point import *

class Line:

    def __init__(self, p0 = Point(0,0), p1 = Point(100, 100), direction=None):
        self.p0 = p0
        self.p1 = p1
        self.direction = direction

        self.getMissingValue()

    @classmethod
    def fromLists(self, p0 = [0,0], p1 = [], direction = []):
        if (p1 == [] and direction == []) or (p1 != [] and direction != []):
            print("Please fill in either a list for p1 or for direction")
        else:
            p0 = Point().fromList(p0)
            p1 = Point().fromList(p1)
            direction = Point().fromList(direction)
            return Line(p0, p1, direction=direction)

    def getMissingValue(self):
        if self.direction == None or self.direction == []:
            x0 = self.p1.x - self.p0.x
            x1 = self.p1.y - self.p0.y
            self.direction = Point(x0, x1)
        else:
            x0 = self.direction.x + self.p0.x
            x1 = self.direction.y + self.p0.y
            self.p1 = Point(x0, x1)

    def getLength(self):
        length = math.sqrt(self.direction.x**2 + self.direction.y**2)

        return length
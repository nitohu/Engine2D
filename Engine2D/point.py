class Point:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    @classmethod
    def fromList(self, l = []):
        if len(l) >= 2:
            return Point(l[0], l[1])
        else:
            # print("The List must include an x and y value: [x, y]")
            pass

    def toList(self):
        return [self.x, self.y]

    def printPosition(self):
        print("(" + str(self.x) + "/" + str(self.y) + ")")
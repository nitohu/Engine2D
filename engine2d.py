import pygame, sys, math

from Engine2D.point import *
from Engine2D.line import *

class Engine2D:

    def __init__(self, width = 600, height = 600, bgColor = (0,0,0)):

        self.width = width
        self.height = height
        self.backgroundColor = bgColor

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        print(type(self.screen))

        self.screen.fill(self.backgroundColor)

    def setWindowTitle(self, title = "Engine2D - A Pygame Engine"):
        pygame.display.set_caption(title)

    def update(self, e = []):
        pygame.display.flip()
        for curr_events in pygame.event.get():
            if curr_events.type == pygame.QUIT:
                sys.exit(0)
    
    def fillScreen(self, color=(0,0,0)):
        self.screen.fill(color)

    def drawPoint(self, point = Point(), color = (255, 255, 255), radius=1):
        pos = point.toList()
        pygame.draw.circle(self.screen, color, pos, radius, 1)
        # pygame.draw.circle(self.screen, (0,0,0), [5, 5], 1, 1)

    def drawLine(self, line = Line(), color = (255, 255, 255)):
        pygame.draw.line(self.screen, color, line.p0.toList(), line.p1.toList(), 1)

    def printSize(self):
        print("(" + str(self.width) + "/" + str(self.height) + ")")
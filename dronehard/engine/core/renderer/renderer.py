from pygame import draw

# Provide functionality for putting interesting stuff on the back of your eye balls
class Renderer():
    def __init__(self, surface):
        print("CTOR called")
        self.m_surface = surface

    def drawPoint(self, position, color):
        print("drawPoint called")
        self.drawLine(self.m_surface, position, position, color)

    def drawLine(self, startPosition, endPosition, color):
        print("drawLine called")
        draw.line(self.m_surface, color, startPosition, endPosition)

    def drawCircle(self, centerPosition, radius, color):
        draw.circle(self.m_surface, color, centerPosition, radius)

    def drawSprite(self, position, sprite):
        print("drawSprite called")
    
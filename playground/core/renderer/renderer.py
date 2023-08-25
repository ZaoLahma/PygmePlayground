# Provide functionality for putting interesting stuff on the back of your eye balls
class Renderer():
    def __init__(self, surface):
        print("CTOR called")
        self.m_surface = surface

    def drawPoint(self, position, color):
        print("drawPoint called")

    def drawLine(self, startPosition, color):
        print("drawLine called")

    def drawSprite(self, position, sprite):
        print("drawSprite called")
    
import pygame
from engine.core.event.event_quit import EventQuit
from engine.core.event.event_key import EventKeyPressed
from engine.core.event.event_key import EventKeyReleased

# Translate pygame stuff to my stuff
class Window:
    def __init__(self, game, eventDispatcher):
        game.registerRunHook(self.runHook)
        game.registerPreFrameHook(self.preFrameHook)
        game.registerPostFrameHook(self.postFrameHook)
        self.m_eventDispatcher = eventDispatcher
        self.m_windowSize = (800, 600)
        self.m_window = pygame.display.set_mode(self.m_windowSize)

    def getDisplay(self):
        return self.m_window

    # Handle events in every frame
    def runHook(self):
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                self.m_eventDispatcher.addEvent(EventQuit())
            elif pygame.KEYDOWN == event.type:
                self.m_eventDispatcher.addEvent(EventKeyPressed(event.key))
            elif pygame.KEYUP == event.type:
                self.m_eventDispatcher.addEvent(EventKeyReleased(event.key))

    def preFrameHook(self):
        self.m_window.fill((0, 0, 0))

    def postFrameHook(self):
        pygame.display.flip()
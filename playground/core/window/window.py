import pygame
from core.event.event_quit import EventQuit

# Translate pygame stuff to my stuff
class Window:
    def __init__(self, game, eventDispatcher):
        game.registerRunHook(self.runHook)
        self.m_eventDispatcher = eventDispatcher
        self.m_windowSize = (800, 600)
        self.m_window = pygame.display.set_mode(self.m_windowSize)

    # Handle events in every frame
    def runHook(self):
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                print("Quit!")
                self.m_eventDispatcher.addEvent(EventQuit())

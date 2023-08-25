from core.event.event_quit import EventQuit
import time

# The thing that makes all other things do things
class Game():
    def __init__(self, targetFPS, useBusyLoop = True):
        self.m_targetFPS = targetFPS
        self.m_useBusyLoop = useBusyLoop
        self.m_targetFrameTime = 1.0 / self.m_targetFPS
        self.m_runHooks = []
        self.m_running = False

    # The game loop. TODO: Make this run at a predictable rate
    def run(self):
        self.m_running = True
        prevTime = time.perf_counter()
        currentTime = prevTime
        while self.m_running:
            prevTime = currentTime
            currentTime = time.perf_counter()
            deltaTime = currentTime - prevTime
            for runHook in self.m_runHooks:
                runHook()
            if self.m_useBusyLoop:
                while time.perf_counter() < currentTime + self.m_targetFrameTime:
                    pass
            else:
                raise NotImplementedError


    # Ugly-ish hack-ish way of hooking in the Game class to the event handling parts
    def registerEventDispatcher(self, eventDispatcher):
        eventDispatcher.registerEventHandler(self.handleEvent)

    # Provide an opportunity to run code for every frame of the game
    def registerRunHook(self, hook):
        self.m_runHooks.append(hook)

    # React to the events 
    def handleEvent(self, event):
        if EventQuit.EVENT_QUIT == event.getType():
            self.m_running = False
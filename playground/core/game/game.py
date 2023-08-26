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

    # The game loop. Can either use busy loop (hog the CPU until it's time to do stuff) 
    # or sleep (play nice and share the toys)
    # High FPS applications probably want to use the busy loop
    # The end goal is to make sure to keep the frame times consistent
    def run(self):
        self.m_running = True
        prevTime = time.perf_counter()
        currentTime = prevTime
        while self.m_running:
            prevTime = time.perf_counter()

            for runHook in self.m_runHooks:
                runHook()

            currentTime = time.perf_counter()

            if self.m_useBusyLoop:
                while time.perf_counter() < currentTime + self.m_targetFrameTime:
                    pass
            else:
                deltaTimeS = (currentTime - prevTime)
                toSleep = self.m_targetFrameTime - deltaTimeS
                if toSleep > 0:
                    time.sleep(toSleep)
            totalFrameTime = (time.perf_counter() - currentTime) * 1000
            print("Total frame time: " + "{:.4f}".format(totalFrameTime) + "ms")
            fps = 1000 / totalFrameTime
            print("fps: " + "{:.4f}".format(fps))


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
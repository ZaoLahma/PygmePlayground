from core.event.event_quit import EventQuit

# The thing that makes all other things do things
class Game():
    def __init__(self):
        self.m_runHooks = []
        self.m_running = False

    # The game loop. TODO: Make this run at a predictable rate
    def run(self):
        self.m_running = True
        while self.m_running:
            for runHook in self.m_runHooks:
                runHook()

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
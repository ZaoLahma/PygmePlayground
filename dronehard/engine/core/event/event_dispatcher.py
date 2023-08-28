# Throw stuff around without direct dependencies between classes
class EventDispatcher():
    def __init__(self, game):
        self.m_eventHandlers = []
        self.m_events = []
        game.registerRunHook(self.run_hook)

    # TODO, maybe: Event type so that not all listeners need to check what type of event is being thrown at them?
    def registerEventHandler(self, eventHandler):
        self.m_eventHandlers.append(eventHandler)

    def addEvent(self, event):
        self.m_events.append(event)

    # Will be executed for every frame
    def run_hook(self, deltaTime):
        for eventHandler in self.m_eventHandlers:
            for event in self.m_events:
                eventHandler(event)
        self.m_events = []
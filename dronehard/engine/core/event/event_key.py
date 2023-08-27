from engine.core.event.event_base import EventBase

class EventKeyPressed(EventBase):
    EVENT_TYPE = "EventKeyPressed"
    def __init__(self, key):
        self.m_key = key

    def getType(self):
        return EventKeyPressed.EVENT_TYPE

class EventKeyReleased(EventBase):
    EVENT_TYPE = "EventKeyReleased"    
    def __init__(self, key):
        self.m_key = key

    def getType(self):
        return EventKeyReleased.EVENT_TYPE
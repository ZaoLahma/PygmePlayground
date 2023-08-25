from core.event.event_base import EventBase

# Well, you know, quit
class EventQuit(EventBase):
    EVENT_QUIT = "EventQuit"
    def getType(self):
        return EventQuit.EVENT_QUIT
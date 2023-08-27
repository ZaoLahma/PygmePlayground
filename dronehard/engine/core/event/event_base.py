# Avoid duck based implementation
class EventBase():
    def getType(self):
        raise NotImplementedError
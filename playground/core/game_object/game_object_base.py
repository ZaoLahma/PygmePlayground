# TODO: Camera position should offset rendering
class GameObjectBase():
    def __init__(self, position):
        self.m_position = position

    def render(self, renderer):
        raise NotImplementedError
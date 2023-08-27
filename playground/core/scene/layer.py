# TODO: Camera position needs to offset the rendering
class Layer():
    def __init__(self):
        self.m_objects = []

    def addObject(self, object):
        self.m_objects.append(object)

    def render(self, renderer):
        for object in self.m_objects:
            object.render(renderer)
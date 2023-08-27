from core.scene.layer import Layer

# Handle graphics layers
# TODO: Take camera (position) into consideration. Don't render objects that aren't visible
class Scene():
    def __init__(self):
        self.m_layers = []

    # Render each layer in the scene, starting with the first added layer as the
    # bottom most layer
    def renderScene(self, renderer):
        for layer in self.m_layers:
            layer.render(renderer)

    def addLayer(self):
        layer = Layer()
        self.m_layers.append(layer)
        return layer
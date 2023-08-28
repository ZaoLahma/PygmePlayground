class SceneManager():
    def __init__(self, renderer, game):
        self.m_renderer = renderer
        game.registerRunHook(self.renderActiveScene)
        self.m_activeScene = None

    def setActiveScene(self, scene):
        self.m_activeScene = scene

    def renderActiveScene(self, deltaTime):
        if None != self.m_activeScene:
            self.m_activeScene.renderScene(self.m_renderer)
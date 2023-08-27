from core.window.window import Window
from core.game.game import Game
from core.event.event_dispatcher import EventDispatcher

# Test stuff
from core.game_object.game_object_base import GameObjectBase
from core.renderer.renderer import Renderer
from core.scene.scene_manager import SceneManager
from core.scene.scene import Scene

class Circle(GameObjectBase):
    def __init__(self, position):
        GameObjectBase.__init__(self, position)

    def render(self, renderer):
        renderer.drawCircle(self.m_position, 10, (255, 255, 255))


if __name__ == "__main__":
    game = Game(targetFPS = 60, useBusyLoop = False)
    eventDispatcher = EventDispatcher(game)
    game.registerEventDispatcher(eventDispatcher)
    window = Window(game, eventDispatcher)

    # Test stuff
    renderer = Renderer(window.getDisplay())
    sceneManager = SceneManager(renderer, game)
    scene = Scene()
    layer = scene.addLayer()
    layer.addObject(Circle((40, 40)))
    sceneManager.setActiveScene(scene)

    # Fire in the hole
    game.run()

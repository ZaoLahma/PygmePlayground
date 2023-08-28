from engine.core.window.window import Window
from engine.core.game.game import Game
from engine.core.event.event_dispatcher import EventDispatcher
from engine.core.scene.scene_manager import SceneManager
from engine.core.renderer.renderer import Renderer

from game.logic.drone_hard import DroneHard

if __name__ == "__main__":
    game = Game(targetFPS = 60)
    eventDispatcher = EventDispatcher(game)
    game.registerEventDispatcher(eventDispatcher)
    window = Window(game, eventDispatcher)
    renderer = Renderer(window.getDisplay())
    sceneManager = SceneManager(renderer, game)

    droneHard = DroneHard(game, eventDispatcher, sceneManager)

    # Fire in the hole
    game.run()

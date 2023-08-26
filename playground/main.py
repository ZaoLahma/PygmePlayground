from core.window.window import Window
from core.game.game import Game
from core.event.event_dispatcher import EventDispatcher

if __name__ == "__main__":
    game = Game(targetFPS = 60, useBusyLoop = False)
    eventDispatcher = EventDispatcher(game)
    game.registerEventDispatcher(eventDispatcher)
    window = Window(game, eventDispatcher)

    # Fire in the hole
    game.run()

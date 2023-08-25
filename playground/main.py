from core.window.window import Window
from core.game.game import Game
from core.event.event_dispatcher import EventDispatcher

if __name__ == "__main__":
    print("Hello world!")
    game = Game()
    eventDispatcher = EventDispatcher(game)
    game.registerEventDispatcher(eventDispatcher)
    window = Window(game, eventDispatcher)

    game.run()

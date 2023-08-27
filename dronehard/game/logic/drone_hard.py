from engine.core.scene.scene import Scene
from engine.core.event.event_key import EventKeyPressed
from game.objects.drone import Drone

class DroneHard():
    def __init__(self, game, eventDispatcher, sceneManager):
        game.registerRunHook(self.runHook)
        eventDispatcher.registerEventHandler(self.handleEvent)
        self.m_sceneManager = sceneManager
        self.m_scenes = []
        self.m_player = Drone((320, 240))

        self.m_scenes.append(Scene())
        layer = self.m_scenes[0].addLayer()
        layer.addObject(self.m_player)

        self.m_sceneManager.setActiveScene(self.m_scenes[0])

    def runHook(self):
        self.m_player.update()

    def handleEvent(self, event):
        if event.getType() == EventKeyPressed.EVENT_TYPE:
            #print(event.m_key)
            if 119 == event.m_key:
                self.m_player.accY(-0.5)
            elif 97 == event.m_key:
                self.m_player.accX(-0.5)
            elif 115 == event.m_key:
                self.m_player.accY(0.5)
            elif 100 == event.m_key:
                self.m_player.accX(0.5)
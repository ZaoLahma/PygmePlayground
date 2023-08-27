from engine.core.game_object.game_object_base import GameObjectBase

class Drone(GameObjectBase):
    def __init__(self, position):
        GameObjectBase.__init__(self, position)
        self.m_movement = (0, 0)

    def render(self, renderer):
        renderer.drawCircle(self.m_position, 10, (255, 255, 255))
    
    def accX(self, acc):
        if self.m_movement[0] < 2 and acc > 0 or self.m_movement[0] > -2 and acc < 0:
            self.m_movement = (self.m_movement[0] + acc, self.m_movement[1])

    def accY(self, acc):
        if self.m_movement[1] < 2 and acc > 0 or self.m_movement[1] > -2 and acc < 0:
            self.m_movement = (self.m_movement[0], self.m_movement[1] + acc)

    def update(self):
        self.m_position = (self.m_position[0] + self.m_movement[0], self.m_position[1] + self.m_movement[1])
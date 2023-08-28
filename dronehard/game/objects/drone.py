from engine.core.game_object.game_object_base import GameObjectBase

class Drone(GameObjectBase):
    ACCELERATION_PER_FRAME = 0.1
    def __init__(self, position):
        GameObjectBase.__init__(self, position)
        self.m_movement = [0, 0]
        self.m_direction = [0, 0]
        self.m_accX = 0.0
        self.m_accY = 0.0

    def render(self, renderer):
        renderer.drawCircle(self.m_position, 10, (255, 255, 255))

    def setAccXDirection(self, direction):
        self.m_direction[0] = direction

    def setAccYDirection(self, direction):
        self.m_direction[1] = direction

    def update(self):
        if self.m_direction[0] == 1:
            self.m_accX += Drone.ACCELERATION_PER_FRAME
        elif self.m_direction[0] == -1:
            self.m_accX -= Drone.ACCELERATION_PER_FRAME
        elif self.m_direction[0] == 0:
            if self.m_accX > 0:
                self.m_accX -= Drone.ACCELERATION_PER_FRAME / 4
            elif self.m_accX < 0:
                self.m_accX += Drone.ACCELERATION_PER_FRAME / 4

        if self.m_direction[1] == 1:
            self.m_accY += Drone.ACCELERATION_PER_FRAME
        elif self.m_direction[1] == -1:
            self.m_accY -= Drone.ACCELERATION_PER_FRAME
        elif self.m_direction[1] == 0:
            if self.m_accY > 0:
                self.m_accY -= Drone.ACCELERATION_PER_FRAME / 4
            elif self.m_accY < 0:
                self.m_accY += Drone.ACCELERATION_PER_FRAME / 4

        self.m_position[0] += self.m_accX
        self.m_position[1] += self.m_accY
        
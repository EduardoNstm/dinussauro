from dino_runner.components.obstacles.obstacles import Obstacle
from random import randint


class Cactus(Obstacle):
    def __init__(self, image):
        self.type = randint(0, 5)
        super().__init__(image, self.type)
        if self.type < 3:
            self.rect.y = 325
        else: 
            self.rect.y = 299
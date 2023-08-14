
from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacles import Obstacle
from dino_runner.components.obstacles.cactus import Cactus


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 6
        super().__init__(image, self.type)
        self.bird_rect = self.image.get_rect()
        self.bird_rect.y = 110
        self.step_index = 0

    def Fly(self):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.bird_rect = self.image.get_rect()
        self.bird_rect.y = 110
        self.step_index += 1

    

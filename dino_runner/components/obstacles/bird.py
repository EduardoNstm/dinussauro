from random import randint
from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacles import Obstacle


class Bird(Obstacle):
    def __init__(self, image):
        bird_posicion = randint(0,2)
        self.type = 0
        super().__init__(image, self.type)
        if bird_posicion == 0:
            self.rect.y = 220
        elif bird_posicion == 1:
            self.rect.y = 250
        elif bird_posicion == 2:
            self.rect.y =  320

        self.step_index = 0
    def draw(self, screen):
        if self.step_index >= 10:
            self.step_index = 0
        screen.blit(self.image[self.step_index<5], self.rect)
        self.step_index += 1
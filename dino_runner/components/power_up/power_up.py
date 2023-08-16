from pygame.sprite import Sprite
from random import randint
from dino_runner.utils.constants import SCREEN_WIDTH


class PowerUp(Sprite):
    def __init(self, image, _type):
        self.image = image
        self.type = _type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + randint(800, 1000)
        self.rect.y = randint(125, 175)
        self.star_up = 0
        self.duration = randint(5, 10)

    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            power_ups.pop()


    def draw(self, screen):
        screen.blit(self.image, self.rect)
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH


class Obstacle(Sprite):
    def __init__(self, image, _type):
        self.image = image
        self.type = _type
        if self.type < 6:
            self.rect = self.image[self.type].get_rect()
        else:
           self.rect = self.image.get_rect()
            
        self.rect.x = SCREEN_WIDTH


    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x  < -self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        if self.type < 6:
            screen.blit(self.image[self.type],(self.rect.x, self.rect.y))  
        else:
            screen.blit(self.image,(self.rect.x, self.rect.y))  
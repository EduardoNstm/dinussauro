import pygame
from random import randint

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS,BIRD
from dino_runner.components.obstacles.bird import Bird

class ObstacleManager:
    def __init__(self):
        self.obstacles = []


    def update(self, game):
        if len(self.obstacles) == 0:
            choice_obstacle = randint(0,3)
            if choice_obstacle >= 2:
                self.obstacles.append(Cactus(SMALL_CACTUS + LARGE_CACTUS))
            else:
                self.obstacles.append(Bird(BIRD))
                  
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
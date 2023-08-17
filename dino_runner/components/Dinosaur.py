import pygame
from dino_runner.utils.constants import (
    RUNNING,
    JUMPING, 
    DUCKING,
    RUNNING_SHIELD, 
    JUMPING_SHIELD,
    DUCKING_SHIELD,
    DEFAULT_TYPE,
    SHIELD_TYPE
)
from pygame.sprite import Sprite
from dino_runner.utils.joystick.joystick import Controler


X_POS = 80
Y_POS = 310
Y_DUCK = Y_POS + 30
JUMP_VEL = 8.5

DUCK_IMG = {
    DEFAULT_TYPE : DUCKING,
    SHIELD_TYPE : DUCKING_SHIELD
    }

JUMP_IMG = {
    DEFAULT_TYPE : JUMPING,
    SHIELD_TYPE : JUMPING_SHIELD
    }

RUN_IMG = {
    DEFAULT_TYPE : RUNNING,
    SHIELD_TYPE : RUNNING_SHIELD
    }

class Dinosaur:
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.jump_vel = JUMP_VEL
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.has_power_up = False
        self.shild = False
        self.show_test = False
        self.power_up_time = 0
        self.joystick = Controler()



    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()
        button_jump = self.joystick.joystick.get_button(0)
        button_duck = self.joystick.joystick.get_button(1)

        if user_input[pygame.K_UP] or button_jump and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] or button_duck and not self.dino_jump:
            self.dino_jump = False
            self.dino_run = False
            self.dino_duck = True
        elif not self.dino_jump:
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck = False

    

        if self.step_index >= 9:
            self.step_index = 0

    def setup_state(self):
        self.has_power_up = False
        self.shild = False
        self.show_test = False
        self.power_up_time = 0

    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMP_IMG[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        if self.dino_duck:
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = X_POS
            self.dino_rect.y = Y_POS + 30
            self.step_index += 1
            dino_duck = False
        

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
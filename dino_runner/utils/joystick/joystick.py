import pygame

class Controler():
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
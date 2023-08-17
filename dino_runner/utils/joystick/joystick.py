import pygame

class Controler():
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    joystick.get_button(0)
    joystick.get_button(1)
    joystick.get_button(7)

    
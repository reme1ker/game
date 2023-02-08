import pygame, movement
from gun import Gun
from pygame.sprite import Group
import random
import os
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

def ebaniyRot():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = [r,g,b]
    return rgb

def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption('Ебашь спермой женщин')
    bg_color = ebaniyRot()
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    movement.create_army(screen, inos)

    while True:
        movement.events(screen, gun, bullets)
        gun.update_gun()
        bullets.update()
        movement.update(bg_color, screen, gun, inos, bullets)
        movement.update_inos(inos)


run()

import pygame
import os
import random

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))




def randomPizda():
    randPizd = 'arts/pizda.png'
    fist_pizda = 'arts/pizdenka.png'
    second_pizda = 'arts/pizda.png'
    fird_pizda = 'arts/pizdavalasa.png'
    four_pizda = 'arts/pizdas.png'
    x = random.randint(1, 4)
    if x == 1:
        randPizd = fist_pizda
    if x == 2:
        randPizd = second_pizda
    if x == 3:
        randPizd = fird_pizda
    if x == 4:
        randPizd = four_pizda
    print(randPizd)
    return randPizd


class Ino(pygame.sprite.Sprite):
    '''класс одного противника'''

    def __init__(self, screen):
        '''инициализация и начальная позиция'''
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(randomPizda())
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        '''Вывод пизды'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''перемещение пизды'''
        self.y += 0.1
        self.rect.y = self.y

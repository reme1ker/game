import pygame
import os
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

class Gun():

    def __init__(self, screen):
        """Инициализация пушки"""

        self.screen = screen
        self.image = pygame.image.load(f'{ROOT_PATH}/arts/pixil-frame-0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        '''отрисовка пушки'''

        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        '''перемещение члена'''
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        if self.mleft and self.rect.left >0:
            self.center -= 1.5

        self.rect.centerx = self.center

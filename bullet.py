import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        '''Сперма'''
        super(Bullet, self).__init__()
        self.screen = screen
        # self.rect = pygame.Rect(0, 0, 2, 12)
        # self.color = 12, 120, 2
        self.image = pygame.image.load('C:/Users/stank/PycharmProjects/game/arts/pulka_1.png')
        self.rect = self.image.get_rect()
        self.speed = 0.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        '''Выстрел мужчины'''
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        '''Рисуем сперму на экране'''
        # pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.rect)

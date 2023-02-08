import pygame

class Ino(pygame.sprite.Sprite):
    '''класс одного противника'''

    def __init__(self, screen):
        '''инициализация и начальная позиция'''
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('arts/pizdenka.png')
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
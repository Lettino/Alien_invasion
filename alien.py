import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #加载外星人图像
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        #设置外星人初始位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #存储外星人的位置
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)
import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):#加载初始设置，绘制的屏幕，飞船类
        super(Bullet,self).__init__()
        self.screen = screen#指定飞船要绘制在什么地方

        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)#创建一个矩形
        self.rect.centerx = ship.rect.centerx#centerx是宽度位置的一半
        self.rect.top = ship.rect.top#设置从顶端飞出

        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        #更新子弹位置的小数值
        self.y -=self.speed_factor
        #更新子弹rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        #绘制子弹
        pygame.draw.rect(self.screen,self.color,self.rect)

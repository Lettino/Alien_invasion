import pygame
from pygame.sprite import Group

from game_stats import GameStats
from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings,screen)
    bullets = Group()#group是pygame中的一种编组实例
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    # 开始游戏的主循环
    stats = GameStats(ai_settings)
    while True:
        # 更新屏幕
        gf.check_events(ai_settings,screen,ship,bullets)#相应飞船事件
        if stats.game_active:
            ship.update()
            # 删除已经消失的子弹
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)  # 绘制图像
        # print(len(bullets))

run_game()



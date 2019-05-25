import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf


def run_game():
    # 初始化游戏并简历屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 飞船
    ship = Ship(ai_settings, screen)
    # 创建存储子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)

        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()

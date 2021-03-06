import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个外星人的类"""

    def __init__(self, ai_settings, screen):
        """初始化外星人并设置初始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        """加载图像"""
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        """在左上角加载外星人"""
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """向左或右移动"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """在指定位置绘制"""
        self.screen.blit(self.image, self.rect)

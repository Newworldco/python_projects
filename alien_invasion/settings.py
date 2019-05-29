class Settings():
    def __init__(self):

        # 屏幕设置
        self.screen_width = 1300
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 子弹设置

        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # 外星人设置
        self.fleet_drop_speed = 100
        # 表示移动方向 1 表示向右，-1 表示向左
        self.fleet_direction = 1

        # 飞船设置

        self.ship_limit = 3

        # 加快游戏节奏
        self.speedup_scale = 2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):

        self.bullet_speed_factor = 8
        self.alien_speed_factor = 3
        self.ship_speed_factor = 10.0

        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度设置"""

        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.ship_speed_factor *= self.speedup_scale



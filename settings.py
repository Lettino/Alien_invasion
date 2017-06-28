class Settings():
    def __init__(self):
        # 初始化屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        #飞船设置
        self.ship_limit = 3#玩家拥有的飞船数量
        self.ship_speed_factor = 1.5
        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #设置方向，1表示向右，-1表示向左
        self.fleet_direction = 1
        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width =3
        self.bullet_height = 15
        self.bullet_color = 60,60,60#为什么不用加括号
        self.bullet_allow = 3



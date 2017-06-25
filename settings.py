class Settings():
    def __init__(self):
        # 初始化屏幕设置
        self.screen_width = 1200
        self.screen_heigh = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5
        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width =3
        self.bullet_height = 15
        self.bullet_color = 60,60,60#为什么不用加括号
        self.bullet_allow = 3


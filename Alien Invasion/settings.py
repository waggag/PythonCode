class Settings():
	"""存储外星人入侵的所有类"""

	def __init__(self):
		"""初始化屏幕的设置"""
		# 屏幕设置
		self.screen_width = 800
		self.screen_height = 600
        # 设置游戏的背景颜色
		self.bg_color = (230, 230, 230)

        # 飞船的设置
		self.ship_speed_factor = 1.5

		# 子弹设置 创建3像素宽,15像素高的深灰色子弹
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		# ~ 设置子弹的数量
		self.bullets_allowed = 3

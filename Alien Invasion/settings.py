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
		self.ship_speed_factor = 1
		#飞船的初始生命
		self.ship_limit = 3

		# 子弹设置 创建3像素宽,15像素高的深灰色子弹
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		# ~ 设置子弹的数量
		self.bullets_allowed = 3
		
		#外星人设置
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 3
		#fleet_direction为1表示向右移，为-1表示向左移
		self.fleet_direction = 1

class Settings():
	"""存储外星人入侵的所有类"""

	def __init__(self):
		"""初始化游戏的静态设置"""
		# 屏幕设置
		self.screen_width = 800
		self.screen_height = 600

		# 设置游戏的背景颜色
		self.bg_color = (230, 230, 230)

        # 飞船的设置
		self.ship_speed_factor = 1
		self.ship_limit = 3

		# 子弹设置 创建3像素宽,15像素高的深灰色子弹
		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3
		
		#外星人设置
		self.fleet_drop_speed = 5

		#以什么样的速度加快游戏节奏
		self.speedup_scale = 1.1
		#外星人点数提高的速度
		self.score_scale = 1.5
		
		self.initialize_dynamic_settings()
	
	def initialize_dynamic_settings(self):
		"""初始化随游戏进行而发生变化"""
		self.ship_speed_factor = 1.2
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1
		#每个外星人的分数
		self.alien_points = 50
		
		# #fleet_direction为1表示向右移，为-1表示向左移
		self.fleet_direction = 1
	
	def increase_speed(self):
		"""提高速度设置和外星人的点数"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)

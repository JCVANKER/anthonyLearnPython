import pygame

class Ship():
	"""飞船类"""
	
	def __init__(self, ai_settings, screen):
		"""初始化飞船并设置其初始位置"""
		
		self.screen = screen
		self.ai_settings = ai_settings
		
		#加载飞船图像并获取其外接矩形
		#pygame.image.load(filename)返回一个包含图像的surface。
		#[pygame.image.save(img,filename)，把img这个surface保存到filename]
		self.image = pygame.image.load('images\ship.bmp')
		
		#Surface.get_rect()获取Surface对象的外接矩形，返回一个Rect对象
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#将每艘新飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#在飞船的属性center中存储小数值
		self.center = float(self.rect.centerx)
		
		#移动标志
		self.moving_right = False
		self.moving_left = False
	
	def update(self):
		"""根据移动标志调整飞船的位置"""
		
		#检查飞船的位置。self.rect.right返回飞船外接矩形的右边缘的x坐标
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		
		#self.rect.centerx只存储self.center的整数部分
		self.rect.centerx = self.center
	def blitme(self):
		"""在指定位置绘制飞船"""
		
		#Draws a source Surface onto this Surface
		#surface.blit(source, dest, area=None, special_flags = 0)->Rect
		#将source(surface)按dest(可以是rect)的位置绘制到surface中
		self.screen.blit(self.image, self.rect)
	

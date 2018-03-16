import pygame
from pygame.sprite import Sprite

"""
	pygame.sprite.Sprite就是Pygame里面用来实现精灵的一个类，使用时，并不需要对它
	实例化，只需要继承它
	
	精灵可以认为成是一个个小图片，一种可以在屏幕上移动的图形对象，并且可以与其他图形对象
	交互。精灵图像可以是使用pygame绘制函数绘制的图像，也可以是原来就有的图像文件。
"""
class Bullet(Sprite):
	"""一个对飞船发射的子弹进行管理的类"""
	
	def __init__(self, ai_settings, screen, ship):
		"""在飞船所处的位置创建一个子弹对象"""
		
		super().__init__()
		self.screen = screen
		
		#在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
			ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		#存储用小树表示的子弹位置
		self.y = float(self.rect.y)
		
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
		
	def update(self):
		"""向上移动子弹"""
		
		#更新表示子弹位置的小数值
		self.y -= self.speed_factor
		#更新表示子弹的rect的位置
		self.rect.y = self.y
		
	def draw_bullet(self):
		"""在屏幕上绘制子弹"""
		
		#pygame.draw.rect(Surface, color, Rect, width=0)
		pygame.draw.rect(self.screen, self.color, self.rect)

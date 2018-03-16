import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	"""初始化游戏并创建一个屏幕对象"""
	
	pygame.init()#initialize all imported pygame modules
	
	ai_settings = Settings()#创建设置实例
	
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	"""
		pygame.display.set_mode(resolution=(0,0), flags=0, depth=0)
		创建显示窗口，分辨率resolution可以是元组也可以是列表
		返回一个surface
	"""
	
	pygame.display.set_caption("Alien Invasion")
	
	#创建一艘飞船	
	ship = Ship(ai_settings, screen)
	
	#创建一个用于存储子弹的编组
	"""
		pygame.sprite.Group类类似于列表，但提供了有助于开发游戏的额外功能
	"""
	bullets = Group()
		
	# 开始游戏的主循环
	while True:
		
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings, screen, ship, bullets)
		

run_game()

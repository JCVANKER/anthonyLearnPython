"""一个可用于表示餐厅的类"""#模块文档字符串

class Restaurant():
	"""模拟餐厅营业情况"""
	
	def __init__(self,restaurant_name,cuisine_type):
		"""初始化属性restaurant_name和cuisine_type"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		"""模拟餐厅简介"""
		print("The restaurant's name is " + self.restaurant_name + ".")
		print("The cuisine type is "+ self.cuisine_type)
	def open_restaurant(self,active):
		"""模拟描述餐厅开业情况"""
		if active == True:
			print(self.restaurant_name + " is opening.")
		else:
			print(self.restaurant_name + " is closing.")

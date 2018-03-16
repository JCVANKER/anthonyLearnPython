class Restaurant():
	"""模拟餐厅营业情况"""
	
	def __init__(self,restaurant_name,cuisine_type):
		"""初始化属性restaurant_name和cuisine_type"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served=0#添加一个属性，并初始化为0
		
	def describe_restaurant(self):
		"""模拟餐厅简介"""
		print("The restaurant's name is " + self.restaurant_name + ".")
		print("The cuisine type is "+ self.cuisine_type)
		
	def set_number_served(self,number):
		"""设置属性number_served的值"""
		if number >= 0:
			self.number_served = number

	def increment_number_served(self,increment_number):
		"""为number_served增加递增量"""
		if increment_number>= 0:
			self.number_served += increment_number
		
	def open_restaurant(self,active):
		"""模拟描述餐厅开业情况"""
		if active == True:
			print(self.restaurant_name + " is opening.")
		else:
			print(self.restaurant_name + " is closing.")
	
	def print_number_served(self):
		"""模拟打印餐厅累计顾客数量"""
		print("number_served: " + str(self.number_served))
		
my_restaurant = Restaurant('中餐厅','中餐')
my_restaurant.describe_restaurant()
my_restaurant.set_number_served(1000)
my_restaurant.print_number_served()
increment = input("Please input today's customer:")
increment = int(increment)
my_restaurant.increment_number_served(increment)
my_restaurant.print_number_served()

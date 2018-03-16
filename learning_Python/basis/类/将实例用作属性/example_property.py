#将实例用作属性
#当属性和方法清单以及文件越来越长时，可能需要将类的一部分作为一个独立的类提取出来，
#将大型类拆分成多个协同工作的小类
class Car():
	"""一次模拟汽车的简单尝试"""
	
	def __init__(self,make,model,year):
		"""初始化描述汽车的属性"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_decriptive_name(self):
		"""返回一个完整的汽车名称信息"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
		
	def read_odometer(self):
		"""打印汽车里程表读数"""
		print("This car has " + str(self.odometer_reading) + " miles "+
			"on it.")
			
	def update_odometer(self,mileage):
		"""设置里程表读数"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer.")	
	
	def increment_odometer(self,miles):
		"""修改里程表读数以添加增量"""
		if miles >= 0:
			self.odometer_reading += miles
	
	def fill_gas_tank(self):
		"""描述汽车用油情况"""
		print("The car need a gas tank!")

#创建小类，从ElectricCar类中拆分出管理电池信息的小类，通过将实例用作属性连接
class Battery():
	"""一次模拟电动汽车电瓶的简单尝试"""
	
	def __init__(self,battery_size=70):#形参可选
		self.battery_size=battery_size
	
	def describe_battery(self):
		"""打印一条描述电瓶容量的消息"""
		print("This car has a " + str(self.battery_size) + "-kWh "+
			"battery.")
	
	def alter_battery_size(self,battery_size):
		if battery_size == 85:
			self.battery_size = battery_size
	
	def get_range(self):
		"""打印一条信息，指出电瓶的续航里程"""
		if self.battery_size == 70:
			range = 240#range为临时变量，非属性
		elif self.battery_size == 85:
			range = 270
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)

#创建子类
class ElectricCar(Car):#类的参数括号内为父类
	"""电动汽车的独特之处"""
	
	#子类方法__init__内包含方法super().__init__调用方法的初始化方法，其中不含self
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery = Battery()#将实例用作属性
	
	def fill_gas_tank(self):
		"""重写父类方法，描述电动车不需要油箱"""
		print("The car doesn't need a gas tank!")

my_tesla_car = ElectricCar('tesla','model s',2016)
my_tesla_car.get_decriptive_name()
my_tesla_car.battery.describe_battery()
my_tesla_car.battery.get_range()
#my_tesla_car.battery.battery_size=85	#实例作为属性可修改类中的属性
my_tesla_car.battery.alter_battery_size(85)#通过方法修改属性
my_tesla_car.battery.get_range()

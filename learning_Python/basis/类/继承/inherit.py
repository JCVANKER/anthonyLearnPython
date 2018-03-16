#创建父类（超类superclass）
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

#创建子类
class ElectricCar(Car):#类的参数括号内为父类
	"""电动汽车的独特之处"""
	
	#子类方法__init__内包含方法super().__init__调用方法的初始化方法，其中不含self
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery_size = 70#添加一个属性，初始化值为70
			
	def describe_battery(self):
		"""打印一条描述电瓶容量的信息"""
		print("This car has a " + str(self.battery_size) + "-kWh " +
			"battery.")
	
	def fill_gas_tank(self):
		"""重写父类方法，描述电动车不需要油箱"""
		print("The car doesn't need a gas tank!")
			
my_tesla = ElectricCar('tesla','model s','2016')
print(my_tesla.get_decriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
#创建子类时，父类必须包含在当前文件中，且位于子类前面
#定义子类时，必须在括号内指定父类的名称

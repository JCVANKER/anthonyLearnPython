"""
	修改属性的值：
		1.直接通过实例进行修改
		2.通过方法进行设置
		3.通过方法进行递增
"""

#1.直接通过实例进行修改
class Car():
	"""一次模拟汽车的简单尝试"""
	
	def __init__(self,make,model,year):
		"""初始化描述汽车的属性"""
		self.make=make
		self.model=model
		self.year=year
		self.odometer_reading=0#添加一个属性，初始化为0，不需要在实例中给予实参
	
	def get_descriptive_name(self):
		"""返回整洁的描述性信息"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
		
	def read_odometer(self):#访问属性dometer_reading的方法
		"""打印一条指出汽车里程的信息"""
		print("This car has " + str(self.odometer_reading) + " miles " +
			"on it")

my_new_car = Car('audi','a4',2016)#包含了属性odometer_reading
my_new_car.get_descriptive_name()
my_new_car.read_odometer()
my_new_car.odometer_reading=23#给属性赋值
my_new_car.read_odometer()
print("-----------------------------")

#2.通过方法进行设置
class Car1():
	"""一次模拟汽车的简单尝试"""
	
	def __init__(self,make,model,year):
		"""初始化描述汽车的属性"""
		self.make=make
		self.model=model
		self.year=year
		self.odometer_reading=0#添加一个属性，初始化为0，不需要在实例中给予实参
	
	def get_descriptive_name(self):
		"""返回整洁的描述性信息"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	
	def updata_odometer(self,mileage):
		"""将里程表读数设置为指定的值"""
		if mileage >= self.odometer_reading:#防止回调
			self.odometer_reading=mileage
	
	def read_odometer(self):#访问属性dometer_reading的方法
		"""打印一条指出汽车里程的信息"""
		print("This car has " + str(self.odometer_reading) + " miles " +
			"on it")
my_new_car1 = Car1('audi','a5',2017)
my_new_car1.get_descriptive_name()
my_new_car1.read_odometer()
my_new_car1.updata_odometer(26)
my_new_car1.read_odometer()
print("-----------------------------")

#3.通过方法进行递增
class Car2():
	"""一次模拟汽车的简单尝试"""
	
	def __init__(self,make,model,year):
		"""初始化描述汽车的属性"""
		self.make=make
		self.model=model
		self.year=year
		self.odometer_reading=0#添加一个属性，初始化为0，不需要在实例中给予实参
	
	def get_descriptive_name(self):
		"""返回整洁的描述性信息"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
	
	def updata_odometer(self,mileage):
		"""将里程表读数设置为指定的值"""
		if mileage >= self.odometer_reading:#防止回调
			self.odometer_reading=mileage
	
	def increment_odometer(self,miles):
		"""将里程表读数增加指定的量"""
		if miles > 0:
			self.odometer_reading+=miles
	
	def read_odometer(self):#访问属性dometer_reading的方法
		"""打印一条指出汽车里程的信息"""
		print("This car has " + str(self.odometer_reading) + " miles " +
			"on it")

my_new_car2 = Car2('audi','a8',2018)
my_new_car2.get_descriptive_name()
my_new_car2.read_odometer()
my_new_car2.updata_odometer(10000)
my_new_car2.increment_odometer(100)
my_new_car2.read_odometer()

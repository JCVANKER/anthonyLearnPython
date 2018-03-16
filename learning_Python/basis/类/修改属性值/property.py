#给属性指定默认值
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

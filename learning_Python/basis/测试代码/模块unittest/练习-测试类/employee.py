class Employee():
	"""为员工增加年薪"""
	
	def __init__(self,first,last,salary):
		"""初始化员工基本信息"""
		
		self.first = first
		self.last = last
		self.salary = salary
		
	def give_raise(self,increment_salary = 5000):
		"""加薪，默认5000"""
		
		self.salary += increment_salary 
		return self.salary

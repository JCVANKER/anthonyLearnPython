class People():
	"""基类"""
	
	name = ''
	age = 0
	__weight = 0 #私有属性
	
	def __init__(self,n,a,w):
		self.name = n
		self.age = a
		self.__weight = w
		
	def speak(self):
		print("%s 说： 我 %d 岁了"%(self.name,self.age))
	
	def __str__(self):
		return "%s 说： 我 %d 岁了"%(self.name,self.age)

class Student(People):
	"""子类"""
	
	grade = ''
	def __init__(self,n,a,w,g):
		#调用父类的构造函数
		People.__init__(self,n,a,w)
		self.grade = g
	
	#重写父类的方法
	def speak(self):
		print("%s 说： 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
s = Student('Anthony',21,57,3)
s.speak()

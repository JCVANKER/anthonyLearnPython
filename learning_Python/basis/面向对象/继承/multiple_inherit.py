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
		
class Speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))
        
#多重继承
class Sample(Speaker,Student):
	a = ''
	def __init__(self,n,a,w,g,t):
		Speaker.__init__(self,n,t)
		Student.__init__(self,n,a,w,g)
	
s = Sample('Anthony',21,57,3,'Python')
s.speak()#方法名同，默认调用的是在括号中排前地父类的方法

#http://www.runoob.com/python3/python3-class.html

#根据约定，类的名称首字母大写
class Dog():
	"""一次模拟小狗的简单尝试"""
								#类中空一行分隔方法；在模块中，空两行分隔函数
	def __init__(self,name,age):
		"""初始化属性name和age"""
		self.name = name
		self.age = age
	
	def sit(self):
		"""模拟小狗被命令时蹲下"""
		print(self.name.title() + " is now sitting.")
	
	def roll_over(self):
		"""模拟小狗被命令时打滚"""
		print(self.name.title() + " rolled over!")
"""
	方法__init__()是一个特殊的方法，每当创建新实例时，Python会自动运行它，开头末尾各
	有两个下划线；形参self不可少，且位于其他形参的前面，创建实例时，自动传入实参self，
	每个与类相关联的方法调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够
	访问类中的属性和方法；
"""
#创建实例
my_dog = Dog('willie',6)
print("My dog's name is " + my_dog.name.title() + ".")#访问属性
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()#访问方法
my_dog.roll_over()

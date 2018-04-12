#自定义异常类应该继承自 Exception 类，或者直接继承，或者间接继承
#在该例子中，类 Exception 默认的 __init__() 被覆盖
class MyError(Exception):
	"""自定义异常"""
	
	def __init__(self,value):
		self.value = value
	
	def __str__(self):
		return repr(self.value)
		
try:
	raise MyError(2)
except MyError as m:	# m是异常类MyError的对象
	print(m.value)

raise MyError("opp")	# 抛出异常时，调用__str__函数，返回return语句
"""
	执行raise语句时，Python会创建指定的异常类的一个对象。raise语句还可指定对异常对象
	进行初始化的参数。
"""

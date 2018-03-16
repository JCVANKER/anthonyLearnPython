from random import randint
#randint(start,stop)返回从start到stop的随机数，包含start和stop

class Die():
	"""模拟骰子"""
	
	def __init__(self,sides=6):
		"""初始化骰子的面数"""
		self.sides = sides
	
	def roll_die(self,n):
		"""打印投掷骰子的结果"""
		
		i=1
		while i <= n:
			print("第" + str(i) + "次投掷的结果是：" + 
				str(randint(1,self.sides)))
			i+=1
			
six_sides_die = Die(6)
six_sides_die.roll_die(10)
print("--------------------------------------")
ten_sides_die = Die(10)
ten_sides_die.roll_die(10)
print("--------------------------------------")
twenty_sides_die = Die(20)
twenty_sides_die.roll_die(10)

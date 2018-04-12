"""
	finally子句定义了无论在任何情况下都会执行的清理行为。
	不管有没有发生异常，finally子句都会执行。
	
	如果一个异常没有被 except 子句截住，那么先执行finally语句在将异常抛出
"""

try:
	raise KeyboardInterrupt # raise 关键字抛出异常
finally:
	print("KeyboardInterrupt没有被任何except子句截住，先执行finally.")


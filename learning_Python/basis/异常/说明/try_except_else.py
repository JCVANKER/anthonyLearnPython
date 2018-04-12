"""
	else将在try语句没有发生任何异常时执行。
	
	异常处理并不仅仅处理那些直接发生在try子句中的异常，而且还能处理子句中调用的函数
	（甚至间接调用的函数）里抛出的异常。
"""

def dividefunc(a,b):
	"""a/b"""
	
	return a/b

try:
	a = int(input("Please input a number:"))
	b = int(input("Please input another number:"))
	c = dividefunc(a,b)
except ValueError as v:
	print(v)
except ZeroDivisionError as z:
	print(z)
except:
	print("Error")
else:
	print("a / b = {0:.3f}".format(c))
finally:
	print("GoodBye.")#不管有没有发生异常，finally子句都会执行

#如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出。
"""
	执行raise语句时，Python会创建指定的异常类的一个对象。raise语句还可指定对异常对象
	进行初始化的参数。
"""
try:
	raise NameError("Hi.")

except NameError as s:
	print(s)
	raise	# raise 语句不加参数可再次抛出异常。
	

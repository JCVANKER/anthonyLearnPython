def dividefunc(a,b):
	""" a / b """
	
	bool_value = False
	try:
		c = a / b
	except ZeroDivisionError:
		bool_value = True
		print("ZeroDivisionError.")
	else:
		bool_value = True
		print("a / b = " + repr(c))
	finally:
		if bool_value:
			print("当参数是字符串时，异常没有被任何except字句截住。会先执行" +
				"该条语句。\n")
			print("-----------------------------------------------")
		else:
			print("当参数是字符串时，异常没有被任何except字句截住。会先执行" +
				"该条语句。")

dividefunc(1,2)
dividefunc(1,0)
dividefunc('s','s')

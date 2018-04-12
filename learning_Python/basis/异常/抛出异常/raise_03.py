try:
	s = None
	y = None
	if s is None:
		print("s 是空对象。")
		raise NameError #引发异常，余下部分被忽略
	print(len(y))
except TypeError:
	print("空对象没有长度。")
finally:
	print("先执行") #引发NameError异常，但没有except子句截取，先执行finally再异常


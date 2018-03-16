import sys

"""
	迭代器(iterator)是一个可以记录遍历的位置的对象
	迭代器有两个基本的方法：iter() 和 next()
"""
my_list = [x for x in range(1,5)]
it = iter(my_list) #创建迭代器对象
while True:
	try:
		print(next(it), end = " ")
	except StopIteration:
		break
#for x in it:
#	print(x)	方法next()会记录迭代的位置
print("\n---------------------------------")
"""
	使用了 yield 的函数被称为生成器（generator）
	生成器是一个返回迭代器的函数，只能用于迭代操作
	
	在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，
	返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
"""
def fibonacci(n):	#生成器函数(使用了yield) - 斐波那契
	"""斐波那契数列
	
	通过生成器返回一个迭代器的对象，来遍历斐波那契，可避免创建列表占有大量的存储空间"""
	
	a, b, counter = 0, 1, 0
	while True:
		if counter > n :
			return
		yield a
		a, b = b, a+b
		counter += 1

f = fibonacci(10)	# f 是一个迭代器，由生成器返回生成
while True:
	try:
		print(next(f),end = " ")
	except StopIteration:
		sys.exit()

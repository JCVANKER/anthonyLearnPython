from functools import reduce
"""
	Python使用lambda来创建匿名函数。
	lambda的主体是一个表达式，仅仅能在lambda表达式中封装有限的逻辑进去。
	lambda函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
	
"""
f = lambda x: x+1
print(f(1))
print("--------------------------------")

"""
	map() 会根据提供的函数对指定序列做映射。
	第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 
	function 函数返回值的map类（类似迭代器）。
"""
print(map(lambda x,y: x+y,[1,3,5,7,9],[2,4,6,8,10]))#可按参数个数类推
print(list(map(lambda x,y: x+y,[1,3,5,7,9],[2,4,6,8,10])))
#代码不够清晰，尽量少用
print("--------------------------------")

"""
	filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的
	filter类(类似迭代器)
	
	filter(function, iterable)
		function -- 判断函数。
		iterable -- 可迭代对象。
		
	接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，
	然后返回 True 或 False，最后将返回 True 的元素放到filter类(类似迭代器)中。
"""
print(filter(lambda x : x % 2 == 0,range(0,10)))
print(list(filter(lambda x : x % 2 == 0,range(0,10))))
#代码不够清晰，尽量少用
print("--------------------------------")

"""
	reduce() 函数会对参数序列中元素进行累积。使用前必须导入从functools模块导入
	
	函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给reduce中的函数
	function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个
	数据用 function 函数运算，最后得到一个结果。
	
	reduce(function, iterable[, initializer])
		function -- 函数，有两个参数
		iterable -- 可迭代对象
		initializer -- 可选，初始参数
	如果不给出initializer, 则第一次调用传递iterable的两个元素, 以后把前一次调用的
	结果和iterable的下一个元素传递给function. 如果给出initializer, 则第一次传递
	initializer和iterable的第一个元素给function.
"""
print(reduce(lambda x, y: x+y, [1,2,3,4,5]))

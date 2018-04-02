#http://www.runoob.com/python3/python3-function.html
#https://blog.csdn.net/wentyoon/article/details/53301594
"""
	L （Local） 局部作用域 
	E （Enclosing） 闭包函数外的函数中 
	G （Global） 全局作用域 
	B （Built-in） 内建作用域
	
	以 L –> E –> G –>B(里到外)的规则查找
	x = int(2.9)  # 内建作用域
 
	g_count = 0  # 全局作用域
	def outer():
		o_count = 1  # 闭包函数外的函数中
		def inner():
			i_count = 2  # 局部作用域
"""

"""
	作用域（Scope）和命名空间（NameSpace）
	scope是由namespace按特定的层级结构组合起来的。scope一定是namespace，
	但namespace不一定是scope。命名空间跟作用域的区别是，它不能在里面再嵌套其他作用域。
	比如def可以在里边嵌套作用域。
	
	模块（Module）、函数(def,lambda)会引入新的作用域，class的定义没
	有作用域，只是创建一个隔离的命名空间，作用类似于作用域；
	
	与C#/Java不同，其它的代码块（如 if/elif/else/、try/except、for/while等）
	是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问。	
"""

#global关键字，声明为全局变量
#当变量为不可变类型时
num = 0
def test_num():
	global num #不声明会报错,根据LEGB原则，报分配前引用错误。
	num += 1
test_num()
print(num)
#当变量为可变类型时
list_num = [0] #列表是可变类型
def test1_num():
	list_num[0] += 1 #编译成功，列表是可变类型，不需要重新生成空间
test1_num()
print(list_num[0])
print("--------------------------------")

#nonlocal关键字，修改嵌套作用域
def outer():
	num = 0
	def inner():
		nonlocal num #不声明会报错
		num += 1
	inner()
	print(num)
outer()
print("--------------------------------")

#进阶题
def counter(start):
	count = [start] # 可变类型，列表
	def internal():
		count[0] += 1 #根据LEGB原则，分配时先找局部变量，由于是可变类型，不需要重新引用
		return count[0]
	return internal
count = counter(0)
#help(counter) internal
#help(counter()) int
for i in range(10):#每次调用时，闭包函数外的函数变量count[0]都被重新赋值
	if i == 9:
		print(count())
	else:
		print(count(), end=",")
count = counter(0)
print(count())

def counter(start):
	count = start 
	def internal():
		nonlocal count # int不可变类型
		count += 1 
		return count
	return internal
count = counter(0)
for i in range(10):
	if i == 9:
		print(count())
	else:
		print(count(), end=",")

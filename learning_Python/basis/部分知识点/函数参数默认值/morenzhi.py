def f(a,L=[]):
	"""函数内部修改了默认参数属性__defaults__，导致逻辑错误"""
	print(f.__defaults__[0])
	# L是对f.__defaults__[0]的引用
	L.append(a)
	return L
   
print(f(1))
print(f(2))
print(f(3))

print("改进----------------------------")

def f1(a,L=None):
	"""取消对默认参数属性__dafaults__的引用，对默认参数重新赋值为具体值"""
	print(f1.__defaults__[0])
	if L == None:
		L = []
	L.append(a)
	return L

print(f1(1))
print(f1(2))
print(f1(3))
"""
	如果在调用一个函数时，没有给默认参数传递值，则函数内的默认参数是对函数的默认参数
	属性__defaults__的引用；
	
	__defaults__是一个元组，第一个默认参数引用__defaults__[0]，以此类推；
	
	__defaults__是可变类型，在函数内部直接修改会导致逻辑错误；
	
	Python的默认参数只会在函数定义时被确定,而不是每次调用时重新确定,所以,一旦在函数中
	修改了默认参数,则再随后的调用中都会生效;
	以函数f(a,L=[])为例子，定义函数时，[]赋值给__defaults__[0]，L是对默认参数属性
	__defaults__[0]的引用，第一次调用时函数内部修改了__defaults__，第二次调用，
	不会将[]重新赋值给__defaults__[0]，而L仍然是对__defaults__[0]的引用；
	
	不允许在函数内部对默认参数引用的类.__defaults__属性进行修改，就在操作默认参数时
	取消它对__defaults__的引用，如函数f1()；
	
	防止默认参数修改函数的__defaults__,需要:
	1.定义默认参数时,最好使用不可变类型.
	2.如果默认参数一定要使用可变类型,那就在函数内部对默认参数重新赋值为可变类型的具体值
"""

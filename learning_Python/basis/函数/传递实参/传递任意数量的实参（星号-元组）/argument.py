#传递任意数量的实参
#	形参名前加*号如*toppings中的*号让Python创建一个空元组，接受任意数量的实参
def make_pizza(*toppings):
	"""打印顾客点的所有配料"""
	print(toppings)
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print("- "+topping)
	print()
make_pizza('pepperoni')
make_pizza('mushroom','green peppers','extra cheese')
print("----------------------------------------------")
"""
	如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。
	Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。
	类似于默认值形参
"""
def make_pizza(size,*toppings):
	"""概述要制作的披萨"""
	print("\nMaking a " + str(size)+
		"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- "+topping)
make_pizza(16,'pepperoni')
make_pizza(18,'mushroom','green peppers','extra cheese')
print("----------------------------------------------")

"""包含一个可表示制作披萨的函数"""

#模块，包含函数make_pizza()
def make_pizza(size,*toppings):
	"""概述要制作的披萨"""
	print("\nMaking a " + str(size) +
		"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- "+topping)

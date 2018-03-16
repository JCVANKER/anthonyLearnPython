#确定列表不为空的基本if语句
request_toppings=['mushrooms','green peppers','extra cheese']
if request_toppings:
	for request_topping in request_toppings:
		if(request_topping == 'green peppers'):
			print("Sorry, we are out of green peppers right now.")
		else:
			print("Adding "+request_topping+".")
	print("Finished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")
print("-------------------------------------------")

#使用多个列表或元组
available_toppings=('mushrooms','olives','green peppers','pepperoni',
'pineapple','extra cheese')
request_toppings=['mushrooms','french fries','green peppers',
'extra cheese']
'''
	1.判断request_toppings是否为空列表
	2.for循环输出添加的配料：
		判断request_toppings中的元素是否存在于元组available_toppings中,若
		存在，则判断是否为青椒，是则输出添加失败，否则成功,若不存在，则添加失败。
'''
if request_toppings:
	for request_topping in request_toppings:
		if(request_topping in available_toppings):
			if(request_topping=='green peppers'):
				print("Sorry, we are out of green peppers right now.")
			else:
				print("Adding "+request_topping+".")
		else:
			print("Sorry, we don't have "+request_topping)
	print("Finished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")

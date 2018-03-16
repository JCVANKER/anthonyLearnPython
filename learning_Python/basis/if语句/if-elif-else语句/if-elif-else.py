#if-elif-else语句
age = 12
if age < 4:	
	price = 0
elif age < 18:	#当if为false时，执行该语句，此时不包含age<4
	price = 5
else:
	price = 10
print("Your admission cost is $"+str(price)+".")
print("--------------------")

#多个elif代码块
age = 66
if age < 4:	
	price = 0
elif age < 18:	#当if为false时，执行该语句，此时不包含age<4
	price = 5
elif age < 65:
	price = 10
else:
	price = 6
print("Your admission cost is $"+str(price)+".")
print("--------------------")

#省略else代码块
age = 66
if age < 4:	
	price = 0
elif age < 18:	#当if为false时，执行该语句，此时不包含age<4
	price = 5
elif age < 65:
	price = 10
elif age>=65:
	price = 6
print("Your admission cost is $"+str(price)+".")
print("--------------------")

#一系列独立的if语句测试多个条件
request_toppings=['mushrooms','extra cheese']
if 'mushrooms' in request_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in request_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in request_toppings:
	print("Adding extra cheese.")
print("\nFinished making your pizza!")
'''
	如果只想执行一个代码块，就使用if-elif-else结构；如果要运行多个代码块，使用一系列
	独立的if语句
'''

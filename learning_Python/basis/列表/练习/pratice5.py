#数到20
for number in range(1,21):
	print(number)
print("-------------------------------")
'''#创建列表，包含数字,使用函数list()
numbers=list(range(1,1000001))
print(numbers)
print("-------------------------------")
#函数min()/max()/sum()
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print("-------------------------------")
#奇数
for number in range(1,20,2):
	print(number)
print("-------------------------------")
'''
#创建列表，3-30内能被3整除
numbers=[]
for number in range(3,31):
	if number%3==0:
		numbers.append(number)
print(numbers)
print("-------------------------------")
#列表解析
numbers=[number for number in range(3,31,3)]
print(numbers)
print("-------------------------------")
#列表解析，列表存储1-10内整数的立方
squares=[number**3 for number in range(1,11)]
print(squares)
print("-------------------------------")
#非列表解析，列表存储1-10内整数的立方
squares=[]
for number in range(1,11):
	squares.append(number**3)
print(squares)

car = 'subaru'
if car == 'subaru':
	print(car=='subaru')
if car != 'audi':
	print(car=='audi')
print("-------------------")
#检查两个字符串相等和不等
str1='abc'
str2='bcd'
print("str1 is equal to str2 ?",str1==str2)
#使用函数lower的测试
user='anthony'
youruser='ANTHONY'
if youruser.lower() == user:
	print("The username has been registered.")
print("-------------------")
#使用关键字and和or的测试
num1=18
num2=22
print(num1>=10 and num2>=22)
print(num1>=22 or num2>=22)
print("-------------------")
#测试特定的值是否包含在列表中
list1=['abc','bcd','def']
print('abc' in list1)
print('acd' in list1) 
print("-------------------")
#测试特定的值是否未包含在列表中
print('abc' not in list1)
print('acd' not in list1)

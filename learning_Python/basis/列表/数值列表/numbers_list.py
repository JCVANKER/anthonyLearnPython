#使用函数range(),从第一个参数值开始数，到第二个参数值停止（不包含第二个参数值）
for number in range(1,3):
	print(number)
print("--------------------------------")
#使用函数range()创建数字列表，将函数range()生成的数字作为函数list()的参数
numbers=list(range(1,11))
print(numbers)
print("--------------------------------")
#函数range()第三个参数指定递增数
numbers=list(range(2,11,2))
print(numbers)
print("--------------------------------")
#python中，两个星号**表示乘方运算
squares=[]
for value in range(1,11):
	square=value**2
	squares.append(square)
print(squares)
print("--------------------------------")
#省略临时参数
squares=[]
for value in range(1,11):
	squares.append(value**2)
print(squares)
print("--------------------------------")
#列表解析
squares=[value**2 for value in range(1,11)]
print(squares)
#函数min()/max()/sum()
digits=list(range(1,10))
digits.append(0)
print(min(digits))
print(max(digits))
print(sum(digits))


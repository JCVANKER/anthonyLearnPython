'''
	Python将不能修改的值称为不可变的，而不可变的列表被称为元组
	string, list, tuple都属于sequence（序列）
	tuples=(1,2,3,...) 或者 tuples = 1,2,3,4,...
	元组的括号有时可以省略，它只是作为元组的区分或者包裹内部元素
	元组中元素不能被修改
'''
tup = 1,2,3,4
print(tup)
tup1 = () #空元组
print(tup1)
tup2 = (20,) #一个元素，后边加逗号，输出时包含空格
print(tup2)
tup3 = (20) #一个元素，打印时不包含空格,此时它是一个int类型的变量而不是元组
print(tup3)
dimensions=(200,50)
#访问元组中元素同访问列表中元素一样
print(dimensions[0])
print(dimensions[1])
print("-------------------------")
#遍历元组
for dimension in dimensions:
	print(dimension)
print("-------------------------")
#由于tuple是不可变类型，改变元组变量，重新分配内存空间，变量指向该新的地址
dimensions=(250,50)
print(dimensions)

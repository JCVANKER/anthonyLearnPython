'''
	Python将不能修改的值称为不可变的，而不可变的列表被称为元组
	tuples=(1,2,3,...)
	元组中元素不能被修改
'''
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

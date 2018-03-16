"""
	enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引
	序列，同时列出数据和数据下标 -- (索引，值)，一般用在 for 循环当中。
	
	enumerate(iterable, [start=0])
		iterable -- 可迭代对象。
		start -- 下标起始位置。
"""
my_list = ['Wuminfeng', '男', 19]
print(list(enumerate(my_list)))
print("----------------------------")

#用于for循环中
numbers = ['one', 'two', 'three']
for i, number in enumerate(numbers):
	print(str(i) + " " + number)

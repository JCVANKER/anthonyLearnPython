"""
	构造函数 dict()
		1. 直接从键值对元组列表中构建字典。
		2. 关键字实参构建字典
"""
#dict(键值对元组列表)，实参是列表，列表的元素是包含有两个元素（键值对）的元组
dict1 = dict([('scope',4139),('guido',4127),('jack',4098)])
print(dict1)

#dict(关键字实参)
dict2 = dict(scope=4139, guido=4127, jack=4098)
print(dict2)

#字典推导式
dict3 ={k:v for k,v in dict2.items()}
print(dict3)
dict4 = {i:v for i,v in enumerate([2,4,6])}
print(dict4)
print("---------------------------------")
#字典推导式 + zip()方法
names = ['scope','guido','jack']
scope = (4139,4127,4098)
dict5 = {x:y for x,y in zip(names,scope)}
print(dict5)

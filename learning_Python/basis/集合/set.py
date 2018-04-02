"""
	https://blog.csdn.net/liang19890820/article/details/72654921
	集合分为两类：
		set: 可变集合  —— 可变的，也可以说是unhashable(不可哈希)的
		frozenset: 不可变集合  —— 不可变的，也可以说是hashable（可哈希）的
"""

"""
	集合(set)是一个无序不重复元素的序列；
	基本功能是进行成员关系测试和删除重复元素；
	创建set：
		1. {value，value}
		2. 构造函数set()，参数为序列:string, list, tuple, set, 可迭代对象如range()
	创建空集合必须用set()而不是用{}，因为{}是用来创建空字典的
"""

#创建空集合
set_test = set()
print(set_test)

#创建集合1
set1 = {1.0,'Python',(1,2,3)}
#元素可以是不同类型，但必须是不可变的类型（可哈希hashable）（numbers,string,tuple）
#set1_1 = {[1,2,3],2,3} TypeError: unhashable type: 'list'
print(set1)

#创建集合2
set2 = set({1.0,'Python',(1,2,3)})
#set2_1 = {};help(set2_1) 是一个空字典
print(set2)
set3 = set(range(1,10))
print(set3)
#print(set3[0])不支持索引和切片

print("-----------------------------")

#集合运算
A = set('abcd')
B = set('cdef')

#子集: 为某个集合中一部分的集合，故亦称部分集合。
C = set('ab')
print(C < A)
print(C.issubset(A))

#并集: 是这些集合的所有元素构成的集合，而不包含其他元素。
print(A | B)
print(A.union(B))

#交集：A 与 B 的差集是所有属于 A 且不属于 B 的元素构成的集合
print(A - B)
print(A.difference(B))

#对称差：两个集合的对称差是只属于其中一个集合，而不属于另一个集合的元素组成的集合
print(A ^ B)

print("-----------------------------")

#虽然集合不能有可变元素，但是集合本身是可变的。
s = {'p','y'}
s.add('t')#add()添加单个元素
print(s)
#update()添加多个元素，update() 可以使用元组、列表、字符串或其他集合作为参数。
s.update(['h','o','n'])
print(s)

print("-----------------------------")

#删除元素: discard() 和 remove()
#如果集合中不存在指定的元素，discard()保持不变，remove()会引发KeyError。
s.discard('n')
print(s)
s.discard('m')
print(s)
s.remove('o')
print(s)

print("-----------------------------")

#pop()随机删除和返回一个项目
print(s.pop())
print(s)

#clear()清空集合
s.clear()
print(s)

print("-----------------------------")

#成员测试
list_numbers = [9,8,9,2,6,5,3,9,3]
set_numbers = set(list_numbers)#删除重复元素
if 9 in set_numbers:
	print("9在集合中")
else:
	print("9不在集合中")
list_numbers = list(set_numbers)
print(list_numbers)

print("-----------------------------")

#集合推导式1
set_1 = set("asdasdasdadzvxzv")#参数为序列:string, list, tuple, set, 可迭代对象如：range()
a = {x for x in set_1 if x not in 'abc'}
print(a)

#print(dir(set3))#方法列表

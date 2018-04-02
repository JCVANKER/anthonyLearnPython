#http://www.runoob.com/python3/python3-data-structure.html
"""
	[表达式 for语句 [多个for语句] [if语句判断]] 中间不加逗号
"""
a = [x for x in range(2,7,2)]
print(a)
b = [x for x in range(2,7) if x % 2 ==0]
print(b)
c = [[x,x*2] for x in a]
print(c)
#多个for语句，逐个运行
vec1 = [2,4,6]
vec2 = [4,3,-9]
vec3 = [x*y for x in vec1 for y in vec2]
print(vec3)
#使用复杂表达式
print([str(round(355/113, i)) for i in range(1, 6)])
print("----------------------------")

#嵌套
matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
	]
print(matrix)
#将3x4矩阵转化为4x3矩阵
matriy = [ [raw[i] for raw in matrix] for i in range(4)]
print(matriy)
print("----------------------------")

#元组推导式：同列表推导式，将中括号改成括号
#字典解析式
mca={"a":1, "b":2, "c":3, "d":4}
dicts={v:k for k,v in mca.items()}
print(dicts)
#集合推导式
set1={i*2 for i in [1,1,2]}
print(set1)
print(set([2, 4]))


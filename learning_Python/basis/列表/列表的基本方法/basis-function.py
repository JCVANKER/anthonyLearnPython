#http://www.runoob.com/python3/python3-data-structure.html
#list.append()、切片a[len(a):]=[x] : 添加元素
a = [1,2,3,4,5,6]
#a.append(7)
a[len(a):] = [7] #使用切片添加元素
print(a)

#list1.extend(list2)扩充列表
b = [8,9,10]
a.extend(b)#扩充列表
#等同于：a[len(a):] = b
print(a)

#list.insert(index,item)插入元素
a.insert(0,0)
a.insert(len(a),11) #等同于添加元素
print(a)

#list.remove()删除元素
a.remove(0) #删除第一个出现的元素，没有则报错
print(a)

#list.pop([index])删除并返回元素
b = a.pop() #删除并返回元素，如何没有参数则删除最后一个元素,参数为列表的索引
print(b)
print(a)
print(a.pop(1))
print(a)

#list.clear()、del list[:]移除列表中所有的项
a.clear()
#del a[:] 和 a[:] = []
#注意del a 是删除对象，a被删除后不存在，引用会报错
print(a)

#list.index()返回元素的索引
a = list(range(0,7))
print(a)
print(a.index(5))

#list.count(x)返回x在列表中出现的次数
b = [1,1,2,3,4,5,6,7]
print(b.count(1))

#list.sort()对列表排序
c = list(range(7,0,-1))
print(c)
c.sort()
print(c)
c.sort(reverse=True)#参数reverse=True倒排
print(c)

#list.reverse()倒排列表中的元素
d = [x for x in range(0,15,2)]
print(d)
d.reverse()
print(d)

#list.copy()返回列表的浅复制，相当于list[:]
e = d.copy()
print(e)
e.append(-1)
print(e)
print(d)

#使用del语句，可通过索引或者切片删除列表元素
del d[0]
print(d)
del d[3:5]
print(d)
del d[:]#清空列表中元素，等同于 d.clear() 和 d[:]=[]
print(d)
#del d 报错


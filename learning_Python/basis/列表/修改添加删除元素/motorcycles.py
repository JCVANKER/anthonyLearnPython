motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
#修改元素
motorcycles[0]='ducati'
print(motorcycles)
#方法append()添加元素到列表末尾
motorcycles.append('ducati')
print(motorcycles)
#方法insert()在列表的任何位置中添加新元素,并将往后的每个元素右移一个位置
motorcycles.insert(0,'ducati')
print(motorcycles)
#从列表中删除元素——1.已知要删除的元素在列表中的位置，使用del语句；
#del list[0:-1]运用切片删除指定位置范围内（不包括末尾索引）的元素
#del list 删除整个数据对象，删除后找不到该对象
del motorcycles[0]
print(motorcycles)
#从列表中删除元素——2.弹出最后一个元素并删除，使用方法pop()
last_owned=motorcycles.pop()
print("The last motorcycle I owned was a "+last_owned.title()+".")
print(motorcycles)
#从列表中删除元素——3.方法pop()添加参数指定删除的元素的索引
first_owned=motorcycles.pop(0)
print("The first motorcycle I owned was a "+first_owned.title()+".")
print(motorcycles)
#从列表中删除元素——4.根据值删除元素——方法remove(),若有多个相同的值，只删除第一个
#出现的值，可使用循环语句删除所有出现的值
too_expensive='yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print(too_expensive+" is too expensive to me.")
motorcycles.remove('suzuki')
print(motorcycles)
#方法.index()，参数为元素，可找出元素所在的索引

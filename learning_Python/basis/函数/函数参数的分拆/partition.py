print(list(range(0,3)))
list_for_partition = [0,3]#列表、元组都可以
print(list(range(*list_for_partition)))
#参数列表分拆，*列表(元组)：将列表元素拆分
print("---------------------------------")

def info_me(name,age,gender):
	"""返回姓名，年龄，性别"""
	
	print("Ma name: " + name.title())
	print("My age: " + str(age))
	print("My gender: " + gender)

dict_info_me = {"name":"WuMinFeng","age":20,"gender":"男"}
info_me(**dict_info_me)
#参数列表分拆，**字典：将字典按关键字参数传递分拆

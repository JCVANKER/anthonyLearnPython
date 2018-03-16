#列表的sort、sorted、reverse方法
cars=['bmw','audi','toyota','subaru']
print(cars)
'''
	使用方法sort()对列表进行永久性排序
'''
#假设列表中值都为小写，方法sort()将列表中元素字母正向排序，并且该修改是永久性的。
cars.sort()
print(cars)
#在方法sort()中传递reverse=True，字母顺序反向排序,该修改是永久性的。
cars.sort(reverse=True)
print(cars)
print("-----------------------------------")
'''
	使用方法sorted()对列表进行临时排序
'''
#函数sorted()按特定顺序排序元素，但不影响列表中元素的原始排序顺序。
cars=['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list:")
print(cars)
#在函数sorted()中传递reverse=True
print("\nHere is the sorted list:")
print(sorted(cars,reverse=True))
print("-----------------------------------")
'''
	使用方法reverse()反转列表中元素
'''
cars=['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)
'''
	方法len()获悉列表的长度
'''
print(len(cars))

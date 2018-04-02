"""
	在Python中，None、任何数值类型中的0、空字符串“”、空元组()、空列表[]、空字典{}都
	被当作False，还有自定义类型，如果实现了__ nonzero __ ()或　__ len __ ()方法
	且方法返回 0 或False，则其实例也被当作False，其他对象均为True。
	
	True  and True    ==> True                True  or True    ==> True
    True  and False   ==> False               True  or False   ==> True
    False and True    ==> False               False or True    ==> True
    False and False   ==> False               False or False   ==> False
    
    逻辑操作符 and 和 or 也称作短路操作符：
    它们的参数从左向右解析，一旦结果可以确定就停止。例如，如果 A 和 C 为真而 B 为假，
    A and B and C 不会解析 C。作用于一个普通的非逻辑值时，短路操作符的返回值通常是
    一个常量
"""
a = 0
b = 2
c1 = a and b
c2 = a or b
print(c1)#短路b，输出0
print(c2)#输出2

#三元运算符，运用短路逻辑
print(bool and a or b)
print(bool and b or a)
#[on_true] if [expression] else [on_false]
print(a if a>b else b)

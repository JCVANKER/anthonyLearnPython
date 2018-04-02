#strings、tuples、numbers、frozenset是不可变对象，list、dict、set是可变对象
"""
	不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再
	让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
	
	可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素
	值更改，本身la没有动，只是其内部的一部分值被修改了。
"""
#传不可变对象实例
def change_immutable(a):
	"""传不可变对象"""
	
	a = 10

b=2
change_immutable(b)
# a和b都同时指向int对象2，在函数体内生成新的int对象10，并让a指向它
print(b) # b仍然是2

#传可变对象实例
def change_mutable(my_list):
	"""传可变对象"""
	
	my_list.append([5,6,7,8]);
	print ("函数内取值: ", my_list)

my_list = [1,2,3,4]
change_mutable(my_list)
print ("函数外取值: ", my_list)

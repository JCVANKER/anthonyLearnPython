"""
	从文件中读取数据
		1. 读取整个文件
		2. 逐行读取
		3. 创建一个包含文件各行内容的列表
"""

#1. 读取整个文件
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())
	#read()到达文件末尾时返回一个空字符串，显示出来就是一个空行
"""
	要以任何方式使用文件，都得先打开他。函数open()接受一个参数：要打开的文件名称
	函数open()返回一个表示文件的对象，并将其存储在as后的变量中
	关键字with在不再需要访问文件后将其关闭（with内代码块），或者使用close()关闭
"""
print("-------------------------------------------")

#2 逐行读取
filename = 'pi_digits.txt'
with open(filename) as file_object:
	for line in file_object:#要以每次一行的方式检查文件，可对文件对象使用for循环
		print(line.rstrip())
		#每行的末尾都有一个换行符，而print语句也会加上一个换行符
print("-------------------------------------------")

#3 创建一个包含文件各行内容的列表，并使用数据
with open(filename) as file_object:
	lines = file_object.readlines()#readlines()将内容的各行存储在列表中

pi_string = ''	
for line in lines:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))
print("-------------------------------------------")
"""
	读取文本文件时，Python将其中的所有文本都解读为字符串。若要成数值，则使用函数int()
"""

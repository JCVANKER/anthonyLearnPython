#1. 读取整个文件
filename = 'learning_python.txt'
with open(filename) as file_object:
	contents = file_object.read()
print(contents.rstrip())
print("--------------------------")

#2. 逐行读取
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip()) 
print("--------------------------")

#创建一个包含文件各行内容的列表
with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	line_replace = line.replace('Python','C')
	print(line_replace.rstrip())

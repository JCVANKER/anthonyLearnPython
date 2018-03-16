#使用模块json存储数据
"""
	JSON数据格式并非Python专用，最初是为JavaScript开发的，随后成为常用格式，这能以
	JSON格式存储的数据与使用其他编程语言的人分享。
"""
import json

#json.dump()接受两个实参：存储的数据、存储数据的文件对象
numbers = [2,4,6,8,10]
filename = 'numbers.json'
with open(filename,'w') as f_obj:
	json.dump(numbers,f_obj)

#json.load()加载存储在JSON格式中的信息，参数为文件对象
filename = 'numbers.json'
with open(filename) as file_object:
	numbers = json.load(file_object)
print(numbers)

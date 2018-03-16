def print_file_contents(filename):
	"""打印文本文件中的内容"""
	try:
		with open(filename) as file_object:
			contents = file_object.read()#字符串
	except FileNotFoundError:
		'''
		msg=("Sorry, the file " + filename + " does'nt exist")
		print(msg)
		'''
		pass
	else:
		animal_names = contents.split()#以空格为分割将字符串转换为列表
		for animal_name in animal_names:
			print(animal_name)
	print()

filenames = ['cats.txt','dogs.txt']
for filename in filenames:
	print_file_contents(filename)

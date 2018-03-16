def count_words(filename):
	"""计算一个文件大致包含多少个单词"""
	try:
		with open(filename) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		'''
		mes = "Sorry, the file " + filename + " does not exist."
		print(mes)
		'''
		pass
		#pass语句使Python什么都不做，且起到占位符的作用。
	else:
		#计算文件大概包含多少个单词
		words = contents.split()
		#方法split()以参数字符串为分隔符将字符串分拆成多个部分存储在列表
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) +
			" words.")

filenames = ['alice.txt','siddhartha.txt','moby_dick.txt',
	'little_women']
for filename in filenames:
	count_words(filename)		

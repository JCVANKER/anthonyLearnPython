def words_count(filename):
	"""计算文本中某个单词出现的次数"""
	try:
		with open(filename) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		print("Sorry, the file " + filename + " doesn't exist.")
		'''
		pass
		'''
	else:
		print(contents.lower().count('the'))

words_count('alice.txt')

def get_formatted_name(first,last,middle = ''):
	"""返回一个格式化的完整姓名，包括中间名"""
	if middle:
		full_name = first + ' ' + middle + ' ' + last
		return full_name.title()
	else:
		full_name = first + ' ' + last
		return full_name.title()


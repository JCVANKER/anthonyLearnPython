#重构，将代码划分为一系列完成具体工作的函数
"""
	函数一：从JSON格式文件中获取用户输入的值，若有则返回值、若无返回None
	函数二：提示用户输入，并将其存储至JSON格式文件中
	函数三：输出函数，从函数一中读值，若有则输出语句一、若无执行函数二并输出
"""

import json

filename = 'favorite_number.json'

def get_stored_number():
	"""从JSON格式文件中获取用户输入的值"""
	
	try:
		with open(filename) as f_obj:
			favorite_number = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return favorite_number
		
def get_new_number():
	"""提示用户输入，并存储"""
	
	favorite_number = int(input("Please input your favorite number: "))
	with open(filename,'w') as f_obj:
		json.dump(favorite_number,f_obj)
		
def print_favorite_number():
	"""输出函数"""
	
	favorite_number = get_stored_number()
	if favorite_number:
		print("I know your favorite number! it is " + 
			str(favorite_number))
	else:
		get_new_number()
		print("The number has been stored. Please run again.")

print_favorite_number()

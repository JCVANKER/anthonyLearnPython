#代码能够正确运行，但可进一步修改，将代码划分为一系列完成具体具体工作的函数，叫重构
#要编写出清晰、易于维护和扩展的代码，这种划分工作必不可少

"""
	函数一：从JSON格式文件中获取用户输入的值，若有则返回值、若无返回None
	函数二：提示用户输入，并将其存储至JSON格式文件中
	函数三：判断二次登陆的用户是否为上次登录的用户，若是输出，若不是执行函数二
	函数四：输出函数，从函数一中读值，若有则输出语句一、若无执行函数二并输出
"""
import json

def get_stored_username():
	"""如果存储了用户名，就获取它"""
	
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""提示用户输入用户名"""

	filename = 'username.json'
	username = input("Please input your name:")
	with open(filename,'w') as f_obj:
		json.dump(username,f_obj)
	return username

def judge_username(username):
	"""判断用户是否为上次登录的用户"""
	
	while True:
		msg = "Username is " + username + ", yes or no (input y/n):"
		confirm = input(msg)
		if confirm == 'y':
			return True
		elif confirm == 'n':
			return False
		else:
			continue
			
def greet_user():
	"""问候用户，并指出其名字"""
	
	username = get_stored_username()#获取用户名
	if username:
		if judge_username(username):
			print("Welcome to you, " + username)
		else:
			username = get_new_username()
			print(username + ", login successful.")
	else:
		username = get_new_username()
		print(username + ", login successful.")
greet_user()

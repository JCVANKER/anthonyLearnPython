#http://www.runoob.com/python3/python3-function.html
#函数定义关键字 def
#文档字符串（docstring）注释，描述函数是做什么的，Python用其生成有关程序函数的文档
def greet_user(username):
	'''显示简单问候语'''#docstring文档字符串
	print("Hello " + username.title() +"!")
#调用函数
greet_user('Anthony')

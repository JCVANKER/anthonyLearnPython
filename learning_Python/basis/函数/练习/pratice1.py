#定义函数
def display_message():
	'''显示内容'''
	print("I have learned how to use function.")
#调用函数
display_message()
print("---------------------------------------")
def favorite_book(title):
	'''显示最喜欢的书本'''
	print("One of my favorite books is "+title.title()+".")
favorite_book('Alice in Wonderland')

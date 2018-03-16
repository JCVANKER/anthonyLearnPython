#在要求很多条件都满足才能继续运行的程序中，可定义一个变量，判断整个程序是否处于活动状态
#标志为True时循环继续，False时循环停止
prompt="Tell me something, and i will repeat it back to you:"
prompt+="\nEnter 'quit' to end the program."
active = True
while active:
	message=input(prompt)
	if message == 'quit':
		active = False
	else:
		print(message+"\n")
print("--------------------------------------")
#break退出循环
prompt="\nPlease enter the name of a city you have visited:"
prompt+="\n(Enter 'quit' when you are finished.)"
while True:
	city=input(prompt)
	if city == 'quit':
		break
	else:
		print("I'd love to go to "+city.title()+"!")
print("--------------------------------------")
#continue忽略循环内以下代码，返回到循环开头
current_number = 0
while current_number <10:
	current_number+=1
	if current_number % 2 == 0:
		continue
	else:
		print(current_number)

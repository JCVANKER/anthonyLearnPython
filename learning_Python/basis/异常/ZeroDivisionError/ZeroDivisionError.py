"""
	异常的特殊对象管理程序执行期间发生的错误
	每当发生让Python不知所措的错误时，都会创建一个异常对象
	try-except代码块：
		如果try代码块中的代码出现错误，执行except，若except指定的错误与引发的错误
		相同，则运行其中的代码；
	try-except-else代码块：
		...;如果try代码块中的代码执行成功，则运行else代码块内代码
	可能引发异常的代码才需要放入try语句中，在try代码块成功执行时才需要运行else代码块
	中的代码。
"""
print("Give me two number, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("\nSecond_number: ")
	if second_number == 'q':
		break
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:#异常对象可以不注明
		print("\nYou can't divide by 0!")
	else:
		print("\n" + str(answer))

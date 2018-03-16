#for循环针对集合中的每个元素的一个代码块，而while循环不断运行，直到指定的条件不满足
current_number=1
while current_number <=5:
	print(current_number)
	current_number+=1
print("--------------------------------------------")
#让用户自己选择退出
prompt="Tell me something, and i will repeat it back to you:"
prompt+="\nEnter 'quit' to end the program."
message=""
while message != 'quit':
	message=input(prompt)
	if message != 'quit':
		print(message + "\n") 

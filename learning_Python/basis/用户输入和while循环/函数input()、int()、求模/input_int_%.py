#函数input()接受一个参数：即要向用户显示的提示或说明；返回用户输入的字符串
message=input("Tell me somethin, and I will repeat it bank to you:")
print("Hello "+message+"!")
print("--------------------------------------------------------------")
prompt="If you tell us who you are,we can personalize the message a"
prompt+="you see"
prompt+="\nwhat is you first name?"
name=input(prompt)
print("Hello "+name.title()+"!")
print("--------------------------------------------------------------")

#函数int()转换为数值
height=input("How tell are you? in inches:")
height=int(height)
if height >= 36:
	print("You are tall enough to ride!")
else:
	print("You will be able to ride when you are a little older.")
print("--------------------------------------------------------------")

#求模运算符
number=input("Enter a number,and i will tell you if it's even or odd:")
number=int(number)
if number % 2 == 0:
	print("The number "+str(number)+" is odd.")
else:
	print("The number ",number," is even.")

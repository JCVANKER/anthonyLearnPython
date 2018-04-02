print("Please input what toppings you want to add:")
active=True#使用标志
toppings=[]#列表存放topping
while active:
	topping=input()
	if topping == 'quit':
		break;
	else:
		toppings.append(topping)
if len(toppings) == 1:
	print("The toppings you have added is:\n"+toppings[0])
elif len(toppings) == 0:
	print("Are you sure?")
else:
	print("The toppings you have added are:")
	for topping in toppings:
		print(topping)
print("------------------------------------------")
prompt="Pleae input your age:\n(Enter 'quit' to quit)"
while True:
	age=input(prompt)
	if age == 'quit':
		break
	age=int(age)
	if age < 3:
		price = 0
	elif age <=12:
		price = 10
	elif age >12:
		price = 15 
	print("The price is $"+str(price)+".")
print("------------------------------------------")

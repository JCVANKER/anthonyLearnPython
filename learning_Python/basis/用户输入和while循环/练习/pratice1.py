car=input("What car do you want? Sir:")
print("Let me see if i can find you a "+car)
print("--------------------------------------")
people=input("How many people? Sir:")
people=int(people)
if people >= 8 :
	print("Sorry sir, there is no seat!")
else:
	print("Come here!")
print("--------------------------------------")
number=input("Please input a number:")
number=int(number)
if number % 10 == 0:
	print("The number "+str(number)+" is 10的整数倍")
else:
	print("The number "+str(number)+" isn't 10的整数倍")

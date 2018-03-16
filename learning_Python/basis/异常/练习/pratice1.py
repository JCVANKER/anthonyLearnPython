print("Please input two numbers:")
print("Enter 'q' to quit.\n")

while True:
		first_number = input("First_number:")
		if first_number == 'q':
			break
		second_number = input("Second_number:")
		if second_number == 'q':
			break
		try:
			sum_number = int(first_number) + int(second_number)
		except ValueError:
			print("Value error,please input again.\n")
		else:
			print("Sum_number:" + str(sum_number) + "\n")

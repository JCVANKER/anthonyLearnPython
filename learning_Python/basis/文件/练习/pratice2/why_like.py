with open('why_like.txt','a') as file_object:
	while True:
		str_why = input("Why do you like Python?('q' to quit):")
		if str_why != 'q':
			file_object.write(str_why + "\n")
		else:
			break

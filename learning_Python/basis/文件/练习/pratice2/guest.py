with open('guest.txt','w') as file_object:
	guest_names = []
	while True:
		guest_name = input("Please input your name('q' to quit):")
		if guest_name != 'q':
			guest_names.append(guest_name.title())
			file_object.write(guest_name.title() + "\n")
		else:
			break
print("----------------------------------------")

while True:
	guest_name = input("Please input your name:")
	if guest_name.title() in guest_names:
		print("Welcome to you, " + guest_name.title())
		with open('guest_book.txt','w') as file_object:
			file_object.write(guest_name.title() + " had came.\n")
	elif guest_name == 'q':
		break
	else:
		print("Sorry, you are not our number.")

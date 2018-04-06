import json
filename = 'favorite_number.json'
favorite_number = int(input("Please input your favorite number: "))
with open(filename,'w') as f_obj:
	json.dump(favorite_number,f_obj)

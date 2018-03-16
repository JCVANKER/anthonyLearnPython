#数字
favorite_numbers={
	'Anthony':6,
	'Luke':7,
	'Frake':2,
	'Samuel':8,
	'Gardon':1,
	}
for name,number in favorite_numbers.items():
	print(name.title()+"'s favorite number is "+str(number))
print("---------------------------------------------------------------")
for name in favorite_numbers.keys():
	print(name.title()+"'s favorite number is ",
		favorite_numbers[name])
print("---------------------------------------------------------------")
#创建一个应该会接受调查的人员名单列表
names=['Anthony','Hai','Luke','Hao','Wu']
for name in names:
	print("Dear "+name)
	if name in favorite_numbers.keys():
		print("Thank you for your coming.")
	else:
		print("Welcome to you.")

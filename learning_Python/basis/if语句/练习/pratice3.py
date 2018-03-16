usernames=['admin','luke','gardon','anthony','frake']
#if语句判断用户名列表是否为空
if usernames:
	for username in usernames:#for循环遍历列表
		if username == 'admin':#if语句判断username是否为admin
			print("Hello admin,would you like to see a status reports")
		else:
			print("Hello "+username+" thank you for logging in again.")
else:
	print("We need to fine some users!")
print("------------------------------------")
#清空用户列表中所有用户名
del usernames[0:]
print(usernames)
print("Successful deleting")
print("------------------------------------")
current_users=['admin','luKe','Gardon','anthony','Frake']
new_users=['admin','anthony','saily','baby','gai']
#将current_users中的元素全部转换为小写
current_users=[current_user.lower() for current_user in current_users]
print(current_users)
#if语句判断用户名列表是否为空
if new_users:
	for new_user in new_users:#遍历new_user列表
		if new_user.lower() in current_users:#判断新用户是否已存在
			print("The username "+new_user+" has already existed.")
		else:
			print("The username "+new_user+" is not used")
else:
	print("new_users is empty.")
print("------------------------------------")
#创建列表
positions=list(range(1,10))
for position in positions:
	if position == positions[0]:
		print(str(position)+"st")
	elif position == positions[1]:
		print(str(position)+"nd")
	elif position == positions[2]:
		print(str(position)+"rd")
	else:
		print(str(position)+"th")

#in关键字：检查特定值是否包含在列表中
request_toppings=['mushrooms','onions','pineapple']
print('mushrooms' in request_toppings)
print('pepperoni' in request_toppings)
print("-------------------------------")
#not in关键字：检查特定值是否不包含在列表中
banner_users=['andrew','carolina','david']
user='marie'
if user not in banner_users:
	print(user.title()+",you can post a response if you wish.")

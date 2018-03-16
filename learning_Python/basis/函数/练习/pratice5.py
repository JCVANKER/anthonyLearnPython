def making_sandwich(*toppings):
	"""打印添加到三明治中的食材"""
	print("\nMaking a sandwich with the following toppings:")
	for topping in toppings:
		print("- "+topping)
making_sandwich('mashroom','green peppers')
print("-----------------------------------")
def build_profile(first,last,**user_info):
	"""创建一个字典，其中包含我们知道的有关用户的一切"""
	profile={}
	profile['firts_name']=first
	profile['last_name']=last
	for key,value in user_info.items():
		profile[key]=value
	return profile
def print_profile(user_profile):
	"""遍历字典"""
	for key in user_profile.keys():
		print(key+": "+str(user_profile[key]))
my_profile=build_profile('Wu','Minfeng',location='Shenzhen',age=20)
print_profile(my_profile)
print("-----------------------------------")
def making_car(factory,model,**info):
	"""返回一辆汽车的相关信息字典"""
	car={}
	car['factory']=factory
	car['model']=model
	for key,value in info.items():
		car[key]=valuie
	return car
car=making_car('走走行',8127)
print(car)

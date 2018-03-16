#	形参名前加**号如**user_info中的**号让Python创建一个空字典，接受任意数量的键-值
def build_profile(first,last,**user_info):
	"""创建一个字典，其中包含我们知道的有关用户的一切"""
	profile={}
	profile['firts_name']=first
	profile['last_name']=last
	for key,value in user_info.items():
		profile[key]=value
	return profile
#遍历字典
def print_profile(user_profile):
	"""遍历字典"""
	for key,value in user_profile.items():
		print(key+": "+value)
user_profile=build_profile('albert','einstein',
							location='princeton',
							field='physics')
#配合关键字实参，将关键字设为键，值设为键的值
print(user_profile)
print_profile(user_profile)

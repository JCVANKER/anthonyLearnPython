#人
info_WuMinfeng={
	'first_name':'Wu',
	'last_name':'Minfeng',
	'age':20,
	'city':'Shenzhen',
		}
info_ZouYunsheng={
	'first_name':'Zou',
	'last_name':'YunSheng',
	'age':20,
	'city':'Shenzhen',
		}
info_LaiJianghao={
	'first_name':'Lai',
	'last_name':'Jianghao',
	'age':20,
	'city':'Shenzhen',
		}				
#创建列表，将三个字典存储在列表中
people=[info_WuMinfeng,info_ZouYunsheng,info_LaiJianghao]
for a_people in people:#遍历
	print(a_people)
print("---------------------------------------------------")
#创建三个宠物字典
XiaoWu={
	'Type':'Dog',
	'age':3,
	'owner':'WuMinfeng',
	'hobby':'eat',
	}
Xiaoxiao={
	'Type':'cat',
	'age':2,
	'owner':'LaiJianghao',
	'hobby':'sleeping',
	}
XiaoFeng={
	'Type':'bird',
	'age':1,
	'owner':'ZouYunsheng',
	'hobby':'crying',
	}
#创建列表，将三个字典存储在列表中
pets=[XiaoWu,Xiaoxiao,XiaoFeng]
for pet in pets:
	print(pet)
print("---------------------------------------------------")
#喜欢的地方字典
favorite_places={
	'WuMinfeng':['Seatle','ShenZhen'],
	'LaiJianghao':['Shenzhen'],
	'ZouYunsheng':['Beijing','Shanghai'],
	}
for name,places in favorite_places.items():
	if len(places) == 1:
		print(name.title()+"'s favorite place is: ")
		print(places[0]+"\n")
	elif len(places) > 1:
		print(name.title()+"'s favorite place are: ")
		for place in places:#places是一个列表
			print(place)
		print("")
	else:
		print(name.title()+" don't like any place.\n")
print("---------------------------------------------------")
#数字字典
favorite_numbers={
	'Anthony':[6,7,8],
	'Luke':[7,8],
	'Frake':[2],
	'Samuel':[8,10],
	'Gardon':[1],
	}
for name,numbers in favorite_numbers.items():
#name是单个键，numbers是值列表
	if len(numbers) == 1:
		print(name.title()+" 's favorite number is:")
		print(numbers[0])
		print()
	elif len(numbers) > 1:
		print(name.title()+" 's favorite numbers are:")
		for number in numbers:
			print(number)
		print()
	else:
		print(name.title()+" don't like any number.")
		print()
print("---------------------------------------------------")
#城市字典
cities={
	'Shenzhen':{
		'country':'China',
		'population':'2000w',
		'fact':'Beautiful',
		},
	'Seatle':{
		'country':'America',
		'population':'500w',
		'fact':'Technology',
		},
	'Shantou':{
		'country':'China',
		'population':'1000w',
		'fact':'Home',
		},	
	}
for city_name,info_city in cities.items():
#.item()以列表的形式返回键、值元组数组
#city_name为单个键，info_city为单个值列表
	print(city_name.title()+":")
	for key,value in info_city.items():
		print(key+": "+value)
	print()
print("---------------------------------------------------")

#在字典中存储字典
users={
	'aeinstein':{
		'first':'albert',
		'last':'einstein',
		'location':'princeton',
		},#记住，字典键-值间用逗号分隔
	'mucrie':{
		'first':'marie',
		'last':'curie',
		'location':'paris',
		}
	}
#遍历
for username,user_info in users.items():
	print("\nusername: "+username)
	print("\tFullname: "+(user_info['first']+user_info['last']).title())
	print("\tLocation: "+user_info['location'])

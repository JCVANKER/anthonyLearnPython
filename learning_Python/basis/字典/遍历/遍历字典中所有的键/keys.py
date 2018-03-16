#遍历字典中所有的键
favorite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}
#.keys()函数以列表的形式返回可遍历的（键）元组数组
#可通过遍历键来获取值，从而遍历字典
#遍历字典默认为.keys()，即dict.keys()与dict相同
for name in favorite_languages.keys():
	print(name+"'s favorite language is "+favorite_languages[name])
print("---------------------------------------------------------------")
#创建列表
friends=['phil','sarah']
for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		print(" Hi "+name.title()+", I see your favorite language is "+
			favorite_languages[name]
			)
print("---------------------------------------------------------------")
#dict.keys()返回一个列表，其中包含字典中的所有键
if 'eric' not in favorite_languages.keys():
	print("Eric, please take our poll!")
print("---------------------------------------------------------------")
#按顺序遍历字典中的所有键，sorted()函数对列表中元素进行排序
for name in sorted(favorite_languages.keys()):
	print("Hi "+name.title()+', thank you for taking the poll.')

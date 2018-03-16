#遍历字典中所有的值
favorite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}
#.values()返回一个值列表
for language in favorite_languages.values():
	print(language.title())
print("---------------------------------------------------------------")
#集合set()剔除重复项
for language in set(favorite_languages.values()):
	print(language.title())

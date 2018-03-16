#在字典中嵌套列表
#每当需要在字典中将一个键关联到多个值时，都可以在字典中嵌套列表

#存储披萨信息
pizza={
	'crust':'thick',
	'toppings':['mushrooms','extra cheese'],#键-列表
	}
print("You ordered a "+pizza['crust']+"-crust pizza "+
	"with the following toppings:")
for topping in pizza['toppings']:#相当于遍历列表
	print("\t"+topping)
print("----------------------------------------------")
#最喜欢的语言
favorite_languages={
	'jen':['python','ruby'],#键-列表
	'sarah':['c'],
	'edward':['ruby','go'],
	'phil':['python','haskell'],
	}
for name,languages in favorite_languages.items():#遍历字典,languages是一个列表
	if len(languages) == 1:
		print(name.title()+"'s favorite language is:")
		print(languages[0].title())
	elif len(languages) >1:
		print(name.title()+"'s favorite language are:")
		for language in languages:#遍历列表
			print(language.title())
	else:
		print(name.title()+" don't like any language.")

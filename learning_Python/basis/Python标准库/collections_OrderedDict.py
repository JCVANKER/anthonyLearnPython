#字典让你能够将信息关联起来，但它们不记录你添加键-值对的顺序
#模块collections中的OrderedDict类创建实例与字典相同，但记录键-值对的顺序
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['anthony'] = 'c'
favorite_languages['sarah'] = 'python'
favorite_languages['phi;'] = 'ruby'

for name,language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language.title())

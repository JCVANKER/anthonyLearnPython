def make_shirt(size,letter):
	'''定制一套T恤'''
	print("size: " + size + "\nletter: " + letter)
#位置实参调用
make_shirt('XXL','Python')
print("-----------------------------------------")
#关键字实参调用
make_shirt(size='XXL',letter='Python')
print("-----------------------------------------")

#默认值
def make_shirt(size='XXL',letter='I love Python'):
	'''定制一套T恤'''
	print("size: " + size + "\nletter: " + letter)
make_shirt()
print("-----------------------------------------")
make_shirt('XL')
print("-----------------------------------------")
make_shirt('L','I love you')
print("-----------------------------------------")


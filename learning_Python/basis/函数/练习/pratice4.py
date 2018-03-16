def show_magicians(magicians):
	"""打印列表中每个魔术师的名字"""
	for magician in magicians:
		print(magician)
magicians=['hannah','ty','margot']
show_magicians(magicians)
print("----------------------------")
'''
def make_great(magicians):
	"""修改列表中的元素，在每个魔术师的名字中都加入字样“The Great”。"""
	for magician in magicians:
		index_magician=magicians.index(magician)#index()找元素在列表中的索引
		changed_magician="The Great "+magician
		magicians[index_magician]=changed_magician
make_great(magicians)
show_magicians(magicians)
print("----------------------------")
'''
def make_great(magicians):
	"""
	修改列表中的元素，在每个魔术师的名字中都加入字样“The Great”。
	返回新的列表
	"""
	for magician in magicians:
		index_magician=magicians.index(magician)#index()找元素在列表中的索引
		changed_magician="The Great "+magician
		magicians[index_magician]=changed_magician
	return magicians
make_great_magicians=make_great(magicians[:])#切片表示法[:]创建列表的副本
show_magicians(make_great_magicians)
print()
show_magicians(magicians)

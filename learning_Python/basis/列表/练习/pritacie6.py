#创建列表
names=['anthony','luke','frake','dick','gardon']
print("The first three items in the list are:")
#切片，for循环打印列表中元素
for name in names[0:3]:
	print(name.title())
print("---------------------------")
print("The items from the middle of the list are:")
for name in names[1:-1]:
	print(name.title())
print("---------------------------")
print("The last three items in the list are:")
for name in names[-3:]:
	print(name.title())
print("---------------------------")
#复制列表并核实
friend_names=names[:]
friend_names.append('you')
names.append('me')
print("friend_names=",friend_names)
print("names=",names)
print("print:")
for name in friend_names:
	print(name)

'''
	切片（有序序列如列表、元组、字符串都有切片）[start:end:step]：
		1. 通过切片访问列表元素
		2. 浅拷贝：通过切片对列表元素添加、修改和删除 a[:] = []
		3. 浅拷贝：复制列表
		4. 浅拷贝：在迭代中修改列表时使用，防止逻辑错误
		
	list[0:-1]不包含最后一个元素
	list[0:]包含最后一个元素
'''
players=['Charles','martina','michael','florence','eli']
print(players[0:3])#输出players列表中索引为0、1、2的元素
print("---------------------------")
#如果没有指定第一个索引，列表将从头开始
print(players[:3])
print("---------------------------")
#如果没有指定末尾索引，切片终止于列表长度lan(list)，包括末尾索引元素，
print(players[2:])
print("---------------------------")
#负数索引返回离列表末尾相应距离的元素,-1为最后一个索引
print(players[-3:])
print("---------------------------")
#当左值大于右值时，返回空字符串，因为[start:end:step]，step默认为1
print(players[1:0])
print("---------------------------")
#当右值溢出时，自动替换为字符串长度
print(players[:8])
print("---------------------------")
# 遍历切片
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())
print("---------------------------")
# 添加、删除元素
players[len(players):] = ['Anthony','Luck'] #右边值为可迭代的对象
print(players)
del players[-2:]
print(players)
print("---------------------------")
# 反向取值
b = players[::-1] # list[start:end:step]
print(b)
'''	
	复制列表:
		一定要用切片：  repeat_list=list[:]	
		不能这样：	repeat_list=list	此时repeat_list和list引用同一个列表
'''
repeat_players=players[:]
print(repeat_players)

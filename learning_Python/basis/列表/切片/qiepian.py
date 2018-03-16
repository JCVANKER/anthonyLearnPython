'''
	切片：处理列表的部分元素
	指定要使用的第一个元素和最后一个元素的索引，不包括最后一个元素
'''
players=['Charles','martina','michael','florence','eli']
print(players[0:3])#输出players列表中索引为0、1、2的元素
print("---------------------------")
#如果没有指定第一个索引，列表将从头开始
print(players[:3])
print("---------------------------")
#如果没有指定末尾索引，切片终止于列表末尾，包括末尾索引元素
print(players[2:])
print("---------------------------")
#负数索引返回离列表末尾相应距离的元素
print(players[-3:])
print("---------------------------")
print("---------------------------")
#	遍历切片
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())
print("---------------------------")
'''	
	复制切片:
		一定要用切片：  repeat_list=list[:]	
		不能这样：	repeat_list=list	此时repeat_list和list指向同一个列表
'''
repeat_players=players[:]
print(repeat_players)

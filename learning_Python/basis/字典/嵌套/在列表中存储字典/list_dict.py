#字典列表，列表元素为字典
alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}
aliens=[alien_0,alien_1,alien_2]#列表
for alien in aliens:#遍历列表
	print(alien)
print("------------------------------------------")
#创建一个用于存储外星人的空列表
aliens=[]
#创建30个绿色的外星人
for aliens_number in range(30):#记录次数
	new_alien={'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)
#显示前5个外星人
for alien in aliens[:5]:#切片
	print(alien)
print("...")
#显示共创建了多少个外星人 len(aliens)
print("Total number of aliens:"+str(len(aliens)))
print("------------------------------------------")
#独立修改列表中字典的元素
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] =10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15
for alien in aliens[:5]:#切片
	print(alien)
print("...")

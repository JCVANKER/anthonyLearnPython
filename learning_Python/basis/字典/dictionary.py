'''
	字典是一系列键-值对，任何python对象都能用作字典中的值,放在{}内。
	键-值间用冒号分割，键-值对之间用逗号分隔。
	列表：list[]
	元组：tuple()
	字典：dictionary{}
'''
#字典元素的访问:dictionary[key]
alien_0={'color':'green','point':5}
new_points=alien_0['point']
print("You just earned "+str(new_points)+" points!")
#添加键-值对:dictionary[key]=value
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)
'''
	键-值对的排列顺序与添加顺序可能不同，Python只关心键和值的关联
'''
print("---------------------------------------------------------------")
#修改字典中的值
alien_1={'x_position':0,'y_position':25,'speed':'medium'}
print("Original x_position: "+str(alien_1['x_position']))
#向右移动外星人，据外星人当前速度决定将其移动多远
if alien_1['speed'] == 'slow':
	x_increment = 1
elif alien_1['speed'] == 'medium':
	x_increment = 2
elif alien_1['speed'] == 'fast':
	x_increment = 3
alien_1['x_position']+=x_increment
print("New x_position: "+str(alien_1['x_position']))
print("---------------------------------------------------------------")
#删除键-值对，使用del语句
del alien_0['point']
print(alien_0)
print("---------------------------------------------------------------")
#由类似对象组成的字典
favorite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}
print("Sarah's favorite language is "+
	favorite_languages['sarah'].title()+"."
	)

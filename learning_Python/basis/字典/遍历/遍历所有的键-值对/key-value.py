#遍历所有的键-值对
user_0={
	'username':'efermi',
	'first':'enrico',
	'last':'fermi',
	}
#items()函数以列表形式返回可遍历的(键, 值) 元组数组
for key,value in user_0.items():#key，value可自定义命名
	print("\nkey: "+key)
	print("\nvalue: "+value)
#键-值对的返回顺序也与存储顺序不同，python不关心键-值对的存储顺序，而只跟踪键-值之间
#的关联关系。

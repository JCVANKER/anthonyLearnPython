'''
	for循环是一种遍历列表的有效方式，但在for循环中不应修改列表，否则将导致Python
	难以跟踪其中的元素。
	while循环可在遍历列表的同时对其进行修改
'''
#创建一个待验证的用户列表
#和一个用于存储已验证用户的空列表
unconfirmed_users=['alice','brian','candace']
confirmed_users=[]
while unconfirmed_users:#列表为空时退出循环
	confirmed_user=unconfirmed_users.pop()#.pop()返回末尾元素并将其存储
	print(confirmed_user)
	confirmed_users.append(confirmed_user)
print("\nThe user you have confirmed are :")
for confirmed_user in confirmed_users:
	print(confirmed_user)
print("----------------------------------------")
#.remove()只能删除列表中第一个出现的特定值
#while循环配合.remove()删除列表中所有特点值元素
pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:#'cat'元素存在于列表pets中时
	pets.remove('cat')
print(pets)
print("----------------------------------------")
#填充字典
responses={}#待填充的空字典
active = True#使用标志
while active:
	name=input("What is your name?")
	response=input("How do you want to resonse?")
	responses[name]=response#填充字典
	repeat=input("Would you like to let another person response?(y/n)")
	if repeat == 'n':
		active = False
print("\n--- Poll Results ---")
for name,response in responses.items():
	print(name.title()+" would like to "+response+".")

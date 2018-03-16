#返回值
def get_formatted_name(first_name,last_name):
	'''返回整洁的姓名'''
	full_name=first_name+' '+last_name
	return full_name
musician=get_formatted_name('jimi','hendrix')
print(musician) 
print("----------------------------------------")

#让实参变成可选，将形参默认值设置成空字符串（无论实参是否为其他类型），并将其置于末尾
def get_formatted_name(first_name,last_name,middle_name=''):
	'''返回整洁的姓名'''
	if middle_name:
		full_name=first_name+' '+middle_name+' '+last_name
	else:
		full_name=first_name+' '+last_name
	return full_name
musician=get_formatted_name('jimi','hendrix')
print(musician)
musician=get_formatted_name('jimi','hendrix','Lee')
print(musician)
print("----------------------------------------")

#返回字典
def build_person(first_name,last_name,age=''):#实参可选，age设为空字符串
	'''返回一个字典，其中包含有关一个人的信息'''
	#创建字典
	person={'first':first_name,'last':last_name}
	if age:
		person['age']=age
	return person
musician=build_person('jimi','hendrix',27)
print(musician)
print("----------------------------------------")

#结合while循环
def get_formatted_name(first_name,last_name):
	'''返回整洁的姓名'''
	full_name=first_name+' '+last_name
	return full_name.title()
while True:
	print("\nPlease tell me your name:")
	print("(Enter 'q' at any time to quit)")
	f_name=input("First name:")
	if f_name=='q':
		break
	l_name=input("Last name:")
	if l_name=='q':
		break
	musician=get_formatted_name(f_name,l_name)
	print("\nHello, " + musician + "!")

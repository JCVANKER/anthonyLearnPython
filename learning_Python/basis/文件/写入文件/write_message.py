"""
	函数open()第二个参数可指定读取模式('r')、写入模式('w')、附加模式('a')或
	读取和写入文件的模式('r+')。默认为读取模式('r')。
	
	若写入的文件不存在，函数open()将自动创建它。
	
	写入模式('w')：如果指定的文件已经存在，Python将在返回文件对象前清空文件。
	附加模式('a')：Python不会再返回文件对象前清空文件，写入的行附加在文件末尾
	
"""
filename = 'programming.txt'

with open(filename,'w') as file_object:
	file_object.write("I love programming.")
	file_object.write("I love creating new games.")
	
#函数write()不会自动在写入的文本末尾添加换行符，换行需要添加换行符\n
with open('programming1.txt','w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")
	
#Python只能将字符串写入文本文件。若要存储数值数据，需使用str()将其转换为字符串
with open('programming2.txt','w') as file_object:
	file_object.write(str(3))

#附加模式('a')
with open('programming1.txt','a') as file_object:
	file_object.write("I also love finding meaningin large datasets.\n")

#f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。
with open('programming3.txt','w') as file_object:
	num = file_object.write("我写了多少个字符？")
print(num)

#f.writelines(sequence),向文件中写入一序列的字符串,换行需写入\n
fobj = open("programming4.txt",'w')
fobj.writelines(["这是第一行\n","这是第二行\n",'这是第三行'])
fobj.close()


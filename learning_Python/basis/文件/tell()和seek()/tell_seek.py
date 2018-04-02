#http://www.runoob.com/python3/python3-inputoutput.html
import math
#f.tell() 获取文件指针的位置，即文件的当前位置，它是从文件开头开始算起的字节数
"""
	f.seek(offset, whence)改变文件当前的位置，whence默认为0：
		seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
		seek(x,1) ： 表示从当前位置往后移动x个字符，文件读写模式需为rb或rb+
		seek(-x,2)： 表示从文件的结尾往前移动x个字符，文件读写模式需为rb或rb+
		
	whence参数的1，2，需将文件的读写模式换成rb或者rb+，否则报错：
	io.UnsupportedOperation: can't do nonzero cur-relative seeks
"""
filename = 'programming.txt'
with open(filename,'w+') as fobj:
	fobj.write('{0:.20f}'.format(math.pi))
#要使用seek()——whence参数的1，2，需将文件的读写模式换成rb或者rb+
with open(filename,'rb+') as fobj:
	fobj.seek(3,0)
	print(fobj.tell())#指针的位置是该字符的前一位
	print(fobj.read(1))#字符'4'是pi的第4位字符，但是它的指针位置是第3位
	fobj.seek(4,1)
	print(fobj.tell())
	print(fobj.read(1))
	fobj.seek(-3,2)#最后一位是空字符，从后往前移动3位其中包含了最有以为空字符
	print(fobj.tell())
	print(fobj.read(2))#f.read(size),size为输出多少位字符


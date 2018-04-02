#http://www.runoob.com/python3/python3-inputoutput.html
"""
	将输出的值转化为字符串: str() repr()
		str(): 函数返回一个用户易读的表达形式。
		repr()： 产生一个解释器易读的表达形式: 1. 包含转义字符 2. 可以是任何对象，如列表等
"""
s = 'Hello world.\n'
print(str(s))
print(repr(s))
print("-------------------------")

list_nums = [1,2,3,4]
# print(str(list_nums))
print(repr((1,2,3,list_nums)))
print("-------------------------")

for i in range(1,11):
	print(repr(i).rjust(2), repr(i*i).rjust(3), end=" ")
	print(repr(i*i*i).rjust(4))
print("-------------------------")

"""
	str.rjust(width[, fillchar]):
		原字符串右对齐，并使用fillchar填充至width长度，若width小于字符串长度则返回原字符串
		width 	 -- 指定填充指定字符后中字符串的总长度.
		fillchar -- 填充的字符，默认为空格。
"""
str="this is string example....wow!!!"
print(str.rjust(50,'0'))
#还有类似的方法, 如 ljust() 和 center()
str="this is string example....wow!!!"
print(str.ljust(50,'1'))
print(str.center(50,'2'))
#zfill(width) 原字符串右对齐，左边填充0
print(str.zfill(50))

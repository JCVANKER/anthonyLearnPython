from sys import argv
#argv参数变量，保存运行Python脚本时传递给Python脚本的参数
script, first, second, third = argv # 解包(unpack)，将所有的参数依次赋值给左边变量
print("fitst: {}".format(first))
print('second: %s' % second)
print('third: ' + third)
"""
	argv和input()的不同点：
		argv是用户在执行命令时要输入的
		input()是脚本运行过程中要输入的
		
	argv和input()参数都是字符串
"""

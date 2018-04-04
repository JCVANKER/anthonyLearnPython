#zip()组合：同时遍历两个或多个序列
#序列：string, tuple, list
names = ['scope','guido','jack']
scope = (4139,4127,4098)
for n,s in zip(names,scope):
	print("What is your {0}, the scope is {1}.".format(n,s))
	
#字典推导式
dic1 = {n:s for n, s in zip(names,scope)}
print(dic1)

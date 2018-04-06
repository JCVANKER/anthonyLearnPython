"""
	https://blog.csdn.net/sxingming/article/details/52164249
	https://www.cnblogs.com/meng-wei-zhi/p/8258531.html
	持久性就是指保持对象，甚至在多次执行同一程序之间也保持对象。
	换句话说：将对象存储在磁盘上，便于以后检索。
	
	对象的持久性：
	如果希望透明地存储 Python 对象，而不丢失其身份和类型等信息，则需要某种形式的对象序列化：
	它是一个将任意复杂的对象转成对象的文本或二进制表示的过程。同样，必须能够将对象经过
	序列化后的形式恢复到原有的对象。在 Python 中，这种序列化过程称为 pickle，可以将
	对象 pickle 成字符串、磁盘上的文件或者任何类似于文件的对象，也可以将这些字符串、
	文件或任何类似于文件的对象 unpickle 成原来的对象。
"""
#pickle提供了一个简单的持久化功能。可以将对象以文件的形式存放在磁盘上。
#pickle模块实现了基本的数据序列和反序列化。
#python中几乎所有的数据类型（列表，字典，集合，类等）都可以用pickle来序列化

#pickle提供四个功能：dumps,dump,loads,load
import pickle

#dumps(obj[,final])返回一个字符串，它包含一个pickle格式的对象（序列化）
data = [1,2,3]
pk1 = pickle.dumps(data,True)#参数True或1，则该参数指定用更快以及更小的二进制表示来创建 pickle
print(pk1)

#loads(obj)返回包含在pickle格式字符串中的对象（反序列化）
dt = pickle.loads(pk1)
print(dt)

"""
	pickle.dump(obj, file[, protocol])
	序列化对象，并将结果数据流写入到文件对象中。参数protocol是序列化模式，默认值为0，
	表示以文本的形式序列化。protocol的值还可以是1或2，表示以二进制的形式序列化。
	
	pickle.load(file)
	反序列化对象。将文件中的数据解析为一个Python对象。
	假如该对象是类的实例，反序列化时必须确保该类的定义存在，否则报错。
"""
#pickle.dump(obj, file[, protocol])
#将类的实例序列化
class Person:
	""""""
	
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def show(self):
		print(self.name + "_", self.age)

anthony = Person('Anthony',22)
anthony.show()
with open('pickle_test.txt','wb+') as fobj:
	pickle.dump(anthony,fobj,1)

#pickle.load(file)
#del Person
with open('pickle_test.txt','rb+') as fobj:
	anthony_unpickle = pickle.load(fobj)
anthony_unpickle.show()
#如果运行del Person将报错

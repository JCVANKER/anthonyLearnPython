class Myclass():
	"""类变量在整个实例化的对象中是公用的"""
	
	i = 1
	def __init__(self):
		self.x = 1

myclass = Myclass()
print('类变量：', Myclass.i)
print('实例变量：', myclass.x)
Myclass.i += 1
print('通过对象去访问类变量： ', myclass.i)
print("再创建一个实例-----")
myclass1 = Myclass()
print('类变量在所有实例化对象中是公用的: ', myclass1.i)
print("---------------------------------------------")

class people:
    #name, age都为类变量
    name = '111'
    age = 0
    #前缀__为私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        #self.name, self.age和以上name, age不同，它们是实例变量
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
# 实例化类
p = people('runoob',10,30)
p.speak()
print('访问类变量： ' + people.name)
#print(p.__weight)外部无法访问私有属性

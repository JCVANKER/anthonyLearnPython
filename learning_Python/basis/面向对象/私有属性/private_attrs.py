
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量 类变量
 
    def count(self):
		#实例变量
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)
 
counter = JustCounter()
counter.count()
counter.count()
print (counter.publicCount)
print (JustCounter.publicCount)#访问类变量，仍然为0
# print (counter.__secretCount)  # 报错，实例不能访问私有变量

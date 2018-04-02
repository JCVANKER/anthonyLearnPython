#将列表当作队列使用，但是效率不高，不推荐使用
#队列使用python内置模块:https://www.cnblogs.com/cmnz/p/6936181.html

#常用双端队列
from collections import deque
dequeue = deque(['Eric','John','Smith'])
print(dequeue)
dequeue.append('Tom') #在右侧（末尾）添加
dequeue.appendleft('jerry') #在左侧（开头）添加
print(dequeue)
dequeue.rotate(2) #循环右移两次
print(dequeue)
print(dequeue.popleft()) #返回并删除左端元素
print(dequeue.pop()) #返回并删除右端元素
print(dequeue)

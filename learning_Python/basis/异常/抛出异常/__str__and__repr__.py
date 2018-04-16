"""
	__str__是显示给用户用的
	__repr__是给机器用的。
	
	print(对象)调用的是__str__方法
	在解释器中直接敲入对象a，调用的是__repr__方法
"""
class A(object):
  def __str__(self):
    print("this is A class")
  def __repr__(self):
    print("this is repr func")
a = A()
print(a)

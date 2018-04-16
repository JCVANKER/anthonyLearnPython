#http://www.runoob.com/python3/python3-errors-execptions.html
"""
	try语句按照如下方式工作:

	1	执行关键字try里面的子句。
	2.1	若没有异常发生，忽略except子句，try子句执行后结束。
	2.2	若执行try子句的过程中发生了异常，那么try子句余下的部分被忽略。如果异常的类型
		和except后的名称相符，那么对应的except子句将被执行。
	3	如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。
	
	一个try语句可包含多个except子句，处理不同的特定的异常。最多只有一个分支会被执行。
	最后一个except子句可以忽略异常的名称，它将被当作通配符使用。
	
	处理程序将只针对对应的try子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。
"""

"""
	一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，例如:

    except (RuntimeError, TypeError, NameError):
        pass
"""

try:
	value = int(input("Please input a number:"))
	print("如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。")
except ValueError:
	print("Your input is not a number")
except:
	print("当作通配符使用。并不是一定会执行这条语句。因为最多只有一个分支被执行。")

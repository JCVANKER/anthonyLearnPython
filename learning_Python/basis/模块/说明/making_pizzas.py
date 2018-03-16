#将函数存储在被称为模块的独立文件中，再将模块导入到主程序中。
#import语句使用模块中的代码


#import语句加模块名，可在程序中使用模块中的所有函数
import pizza
#句点表示法：此时函数的调用方式：module_name.function_name()
pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12,'mushroom','greem peppers','extra cheese')


'''
#导入指定的函数：from module_name import function_0,function_1
from pizza import make_pizza	#函数不加括号
#调用函数时可直接使用函数名
make_pizza(16,'pepperoni')
make_pizza(12,'mushroom','greem peppers','extra cheese')
'''

'''
#使用as给函数指定别名：from module_name import function_name as name
#防止导入的函数的名称与程序中现有的名称冲突，或函数名太长
from pizza import make_pizza as mp
mp(16,'pepperoni')
mp(12,'mushroom','greem peppers','extra cheese')
'''

'''
#使用as给模块指定别名：import module_name as name
import pizza as p
p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushroom','greem peppers','extra cheese')
'''

'''
#星号（*）导入模块中的所有函数
#与不加*号的区别是：调用时不指定模块名
#使用并非自己编写的大型模块时，不要采用这种方法，若Python遇到多个名称相同的函数或变量
#时，会覆盖函数。
from pizza import *
make_pizza(16,'pepperoni')
make_pizza(12,'mushroom','greem peppers','extra cheese')
'''

#最好的做法是：1.只导入自己需要的函数 2.导入整个模块并使用句点表示法。

#函数编写规范：1.多个函数用 两个空格 分开 2.import语句放文件开头，除非有开头注释
#3.若函数参数过多： def function_name(
#								parameter_0,parameter_1,parameter_2,
#								parameter_3,parameter_4,parameter_5,):

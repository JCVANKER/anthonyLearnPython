#单元测试用于核实函数的某个方面没有问题
#测试用例是一组单元测试，这些单元测试一起核实函数在各种情形下都符合要求
#全覆盖式测试用例包含一整套单元测试
"""
	测试未通过时，不要修改测试，而应修复导致测试不能通过的代码；
	检查刚对函数所做的修改，找出导致函数行为不符合预期的修改。
"""

import unittest
#Python标准库中模块unittest提供了代码测试工具
from name_function import get_formatted_name

class NamsTestCase(unittest.TestCase):#必须继承unittest.TestCase类
	"""测试name_function.py"""
	
	def test_first_last_name(self):#单元测试，test_打头的方法自动运行
		"""测试能否正确处理像Janis Joplin这样的姓名"""
		
		formatted_name = get_formatted_name('janis','joplin')
		self.assertEqual(formatted_name,'Janis Joplin')
		#断言方法：用来核实得到的结果是否与期望的结果一致
	
	def test_first_middle_last_name(self):
		"""测试能否正确处理想Janis A Joplin这样的姓名"""
		
		formatted_name = get_formatted_name('janis','joplin','A')
		self.assertEqual(formatted_name,'Janis A Joplin')
		
unittest.main()
#代码行unittest.main()让Python运行这个文件中的测试

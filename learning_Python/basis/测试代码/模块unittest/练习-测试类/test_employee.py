import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""测试Employee类"""

	def setUp(self):#为单元测试创建类对象及共有部分
		"""创建一个雇员对象"""
		self.xiaoming = Employee('xiao','ming',100000)
	
	def test_give_default_raise(self):
		"""测试默认年薪增量"""
		
		new_salary = self.xiaoming.give_raise()
		self.assertEqual(new_salary,105000)
	
	def test_give_custom_raise(self):
		"""测试自定义年薪增量"""
		
		new_salary = self.xiaoming.give_raise(10000)
		self.assertEqual(new_salary,110000)
		
unittest.main()

"""
	部分常用断言方法：	
		assertEqual(a,b)		核实 a==b
		assertNotEqual(a,b)		核实 a!=b
		assertTrue(x)			核实 x为True
		assertFalse(x)			核实	x为False
		assertIn(item,list)		核实item在list中
		assertNotIn(item,list)	核实item不在list中
"""

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""测试AnonymousSurvey类"""
	
	#Python先运行方法setUp()，再运行各个以test_开头的方法。可用来创建对象及共同部分
	def setUp(self):
		"""创建一个调查对象和一组答案，供使用的测试方法使用"""
		
		question = "What language did you first learn to speak?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['English','Spanish','Mandarin']

	def test_store_single_response(self):
		"""测试单个答案会被妥善存储"""
		
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0],self.my_survey.responses)
		
	def test_store_Three_response(self):
		"""测试三个答案会被妥善存储"""
		
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response,self.my_survey.responses)
			
unittest.main()
"""
	运行测试用例时，每完成一个单元测试，Python都打印一个字符：测试通过时打印一个句点；
	测试引发错误时打印一个E；测试导致断言失败时打印一个F
"""

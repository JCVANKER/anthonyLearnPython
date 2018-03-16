import unittest
from city_functions import city_functions

class NamesTestCase(unittest.TestCase):
	"""测试city_functions"""
	
	def test_city_country(self):
		"""测试城市-国家格式"""
		
		city_country = city_functions('santiago','chile')
		self.assertEqual(city_country,'Santiago, Chile')
		#断言方法assertEqual来自于TestCase
		
	def test_city_country_population(self):
		"""测试城市-国家-人口格式"""
		
		city_country_population = city_functions(
			'santiago','chile',5000000)
		self.assertEqual(city_country_population,
			'Santiago, Chile - population 5000000')
			
unittest.main()

def city_functions(city,country,population=''):
	"""返回一个完整的城市信息"""
	
	if population:
		city_country_population = city.title() + ", " + country.title()
		city_country_population += " - population " + str(population)
		return city_country_population
	else:
		city_country = city.title() + ", " + country.title()
		return city_country

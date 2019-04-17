{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

cities = {
	'texas': {
		'country': 'united states',
		'population': 28300000,
		'nearby mountains': 'davis',
		},
	'santiago': {
		'country': 'chile',
		'population': 6158080,
		'nearby mountains': 'andes',
		},
	'kathmandu': {
		'country': 'nepal',
		'population': 1003285,
		'nearby mountains': 'himilaya',
		},
	}

for city, city_info in cities.items():
	country = city_info['country'].title()
	population = city_info['population']
	mountains = city_info['nearby mountains'].title()

	print("\n" + city.title() + " is in " + country + ".")
	print("\t" + "It has a population of about " + str(population) + ".")
	print("\t" + "The " + mountains + " mountains are nearby.")

	
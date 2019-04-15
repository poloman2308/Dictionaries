{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

people = []

person = {
	'first': 'daniel',
	'last': 'stephens',
	'age': 37,
	'city': 'lubbock',
	}

people.append(person)

person = {
	'first': 'derek',
	'last': 'acevedo',
	'age': 32,
	'city': 'abilene',
	}

people.append(person)

person = {
	'first': 'roger',
	'last': 'reyes',
	'age': 40,
	'city': 'san antonio',
	}

people.append(person)

for person in people:
	name = person['first'].title() + " " + person['last'].title()
	age = str(person['age'])
	city = person['city'].title()

	print(name + ", of " + city + ", is " + age + " years old.")



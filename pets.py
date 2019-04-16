{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

pets = []

pet = {
	'animal': 'dog',
	'name': 'presley',
	'owner': 'derek acevedo',
	'city': 'abilene',
	}

pets.append(pet)

pet = {
	'animal': 'cat',
	'name': 'squints',
	'owner': 'derek acevedo',
	'city': 'abilene'
	}

pets.append(pet)

pet = {
	'animal': 'black mamba',
	'name': 'vino',
	'owner': 'kobe bryant',
	'city': 'los angelas',
	}

pets.append(pet)

for pet in pets:
	print("\nHere's what I know about " + pet['name'].title() + ":")
	for key, value in pet.items():
		print("- " + key.title() + ": " + value.title())

					
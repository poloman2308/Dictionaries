{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

favorite_places = {
	'derek': ['bora bora', 'greece', 'fiji'],
	'daniel': ['peru', 'china', 'rome'],
	'roger': ['mexico', 'ireland', 'haiti'],
	}

for name, places in favorite_places.items():
	print("\n" + name.title() + " likes the following places:")
	for place in places:
		print("- " + place.title())

		
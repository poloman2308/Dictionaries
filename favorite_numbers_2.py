{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

favorite_numbers = {
	'derek': [12, 23, 24, 8],
	'daniel': [4, 23, 6, 45],
	'roger': [12, 20, 82, 34],
	}

for name, numbers in favorite_numbers.items():
	print("\n" + name.title() + " likes the following numbers:")
	for number in numbers:
		print("- " + str(number))

		
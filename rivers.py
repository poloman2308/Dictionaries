{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

major_rivers = {
	'nile': 'egypt',
	'amazon': 'brazil',
	'yellow river': 'china',
	}

for river, country in major_rivers.items():
	print("The " + river.title() + " flows through " + country.title() + ".")

print("\nThe following rivers are in the data set:")
for river in major_rivers.keys():
	print("- " + river.title())

print("\nThe following countries are in the data set:")
for country in major_rivers.values():
	print("- " + country.title())


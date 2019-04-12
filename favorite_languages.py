{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

#for name, language in favorite_languages.items():
#	print("\n" + name.title() + "'s favorite language is " + language.title() + ".")

# Looping through all the keys
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")


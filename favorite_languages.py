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

if 'erin' not in favorite_languages.keys():
	print("\nErin, please take the poll!\n")


# Looping through keys in order
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.\n")


# Looping through all the values
print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print("- " + language.title())


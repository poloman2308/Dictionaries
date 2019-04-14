{
	"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}

glossary = {
	'string': 'A series of characters',
	'comment': 'A note in a program that the Python interpreter ignores',
	'list': 'A collection of items in a particular order',
	'loop': 'Work through a collection of items, on at a time',
	'dictionary': 'A collection of key-value pairs',
	}

#word = 'string'
#print("\n" + word.title() + ": " + glossary[word] + ".")

#word = 'comment'
#print("\n" + word.title() + ": " + glossary[word] + ".")

#word = 'list'
#print("\n" + word.title() + ": " + glossary[word] + ".")

#word = 'loop'
#print("\n" + word.title() + ": " + glossary[word] + ".")

#word = 'dictionary'
#print("\n" + word.title() + ": " + glossary[word] + ".")


# Loop through dictionary 
for word, definition in glossary.items():
	print("\n" + word.title() + ": " + definition + ".")


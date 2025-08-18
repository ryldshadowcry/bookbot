#def main():
#	book = get_book_text("./books/frankenstein.txt")
#	words = book.split()
#	wordcount = len(words)
#	allwordsstring = str(words)
#	all_lower = allwordsstring.lower()
#	lowercharactercount = get_lower_character_count(book)
#	countlows = lower_count(lowercharactercount)
#
#
#	print ("============ BOOKBOT ============")
#	print ("Analyzing book found at books/frankenstein.txt...")
#	print ("----------- Word Count ----------")
#	print (f"Found {wordcount} total words")
#	print ("--------- Character Count -------")
#	countlowsprint(countlows)
#	print ("============= END ===============")

def sort_on(items):
	return items["count"]

def lower_count(lowercharactercount):
	list_of_dicts = []
	for character, numb in lowercharactercount.items():
		new_dict = {"char": character, "count": numb}
		list_of_dicts.append(new_dict)
	list_of_dicts.sort(reverse=True, key=sort_on)
	return list_of_dicts

def get_book_text(book):
	with open(book) as text:
		file_contents = text.read()
		return file_contents


def get_lower_character_count(book):
	words = book.split()
	all_lower = book.lower()
	lowercasedictionary = {}
	for letter in all_lower:
		if letter in lowercasedictionary:
			lowercasedictionary[letter] = lowercasedictionary[letter] +1
		else:
			lowercasedictionary[letter] = 1
	return (lowercasedictionary)

def countlowsprint(source):
	for item in source:
		character = item["char"]
		count_value = item["count"]
		if character.isalpha():
			print(f"{character}: {count_value}")

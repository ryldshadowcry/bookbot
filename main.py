import sys
import stats
if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
bookcalled = sys.argv[1]

def main():
#	book = stats.get_book_text("./books/frankenstein.txt")
	book = stats.get_book_text(bookcalled)
	words = book.split()
	wordcount = len(words)
	allwordsstring = str(words)
	all_lower = allwordsstring.lower()
	lowercharactercount = stats.get_lower_character_count(book)
	countlows = stats.lower_count(lowercharactercount)


	print ("============ BOOKBOT ============")
	print (f"Analyzing book found at {bookcalled}...")
	print ("----------- Word Count ----------")
	print (f"Found {wordcount} total words")
	print ("--------- Character Count -------")
	stats.countlowsprint(countlows)
	print ("============= END ===============")


main()

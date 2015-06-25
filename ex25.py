# Ok I will do this one properly, just to practice typing.

def break_words(stuff):
	"""This function breaks stuff into words"""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts list of words alphabetically"""
	return sorted(words)

def print_first_word(words):
	"""removed and prints first word in a list"""
	first = words.pop(0)
	print first

def print_last_word(words):
	"""removes and prints last word in a list"""
	last = words.pop(-1)
	print last

def sort_sentence(sentence):
	"""takes a string sentence and returns sorted list of words"""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""prints first and last word from string sentence"""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)


# dreload(ex25) in ipython is very useful

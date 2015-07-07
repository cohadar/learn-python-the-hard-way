"""Ah this should be mediocre not-interesting."""


_lexicon = {
	'north' : 'direction',
	'south' : 'direction',
	'east' : 'direction',
	'west' : 'direction',
	'go' : 'verb',
	'run' : 'verb',
	'kill' : 'verb',
	'eat' : 'verb',
	'the' : 'stop',
	'in' : 'stop',
	'of' : 'stop',
	'princess' : 'noun',
	'bear' : 'noun',
	'honey' : 'noun',
}


def _find_word_type(word):
	"""return a (TYPE, WORD) tuple or ('error', WORD) is word type is unknown."""
	try:
		return ('number', int(word))
	except ValueError:
		return (_lexicon.get(word.lower(), 'error'), word)

def scan(sentence):
	"""Scans the sentance for words and assigns type to each.

	retuns a list of (TYPE, WORD) tuples
	"""
	words = sentence.split()
	ret = []
	for word in words:
		ret.append(_find_word_type(word))
	return ret

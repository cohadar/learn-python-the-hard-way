"""Parser for stupid game.
Python had problems with this file due to tabs/spaces indent mismatch.
Guess PIP8 is not entirely useless.    
"""


class ParserError(Exception):
    pass


class Sentence(object):
    """Lalalal."""

    def __init__(self, subject, verb, obj):
        self.subject = subject
        self.verb = verb
        self.obj = obj

    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        """Define a non-equality test"""
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        """Override the default hash behavior (that returns the id or the object)"""
        return hash(tuple(sorted(self.__dict__.items())))       
        
    def __repr__(self):
        return "Sentence(subject='%s', verb='%s', obj='%s')" % (self.subject, self.verb, self.obj) 


def peek(word_list):
    """Check to see if a list has a word tuple."""  
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None


def match(word_list, expected_type):
    """Extract head word, if the type matches return worn else None."""
    if word_list:
        word = word_list.pop(0)
        if word[0] == expected_type:
            return word
        else:
            return None
    else:
        return None


def skip(word_list, word_type):
    """skip/discard all words of a certain type from start of the list."""
    while peek(word_list) == word_type:
        match(word_list, word_type)


def parse_verb(word_list):
    """This is just a fancy match verb with exception."""
    skip(word_list, 'stop')
    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")


def parse_object(word_list):
    """Ah finally, a branching in our parser, such complexity."""
    skip(word_list, 'stop')
    next_word = peek(word_list)
    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")


def parse_subject(word_list):
    """Parsing with recursive descent, oh wait..."""
    skip(word_list, 'stop')
    next_word = peek(word_list)
    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")


def parse_sentence(word_list):
    """Oh noes."""
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)
    return Sentence(subj[1], verb[1], obj[1])


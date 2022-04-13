# Ex 25
def break_words(stuff: str):
    """This function will break up words for us."""
    words = stuff.split()
    return words


def sort_words(stuff: list):
    """Sorts the words."""
    return sorted(stuff)


def print_first_word(words: list):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)


def print_last_word(words: list):
    """Prints the last word after popping it off."""
    word = words.pop()
    print(word)


def sort_sentence(sentence: str):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence: str):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence: str):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

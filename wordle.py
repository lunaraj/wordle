import string
import random
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    in_file.close()
    return word_list
WORDLIST_FILENAME = 'words.txt'
### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

class guess(object):
    def __init__(self, guess, word):
        self.guess = guess
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.word = word
    def getGuess(self):
        return self.guess
    def isGuessValid(self):
        if len(self.guess) == 5 and is_word(self.valid_words, self.guess):
            return True
        else:
            return False
    def __str__(self):
        return self.guess[0] + ' ' + self.guess[1] + ' ' + self.guess[2] + ' ' + self.guess[3] + ' ' + self.guess[4]
    def isGuessCorrectHelper(self, i):
        if self.guess[i] == self.word[i]:
            return 'green'
        elif self.guess[i] in self.word:
            return 'yellow'
        else:
            return 'gray'
    
    def isGuessCorrect(self):
        mommy = guess(self.guess, self.word)
        one = mommy.isGuessCorrectHelper(0)
        two = mommy.isGuessCorrectHelper(1)
        three = mommy.isGuessCorrectHelper(2)
        four = mommy.isGuessCorrectHelper(3)
        five = mommy.isGuessCorrectHelper(4)
        return (one, two, three, four, five)


class wordle(object):
    def __init__(self):
        self.valid_words = load_words(WORDLIST_FILENAME)
    def chooseWord(self):
        while True:
            self.word = random.choice(self.valid_words)
            if len(self.word) == 5:
                break
        return self.word
bozo = guess('steph', 'lebro')
print(bozo.isGuessCorrect())

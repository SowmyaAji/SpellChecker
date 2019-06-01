
import re

# open words.txt file which has over 69,000 English words


def get_words():
    words = []
    with open("words.txt") as new_file:
        for word in new_file.readlines():
            word = word.strip()
            words.append(word)
        return words


# check for third consecutive duplicate letter in input and remove it as an autofix (English doesn't have any word with three consecutive duplicates)
def erase_triple_dupes(word):
    return re.sub(r"(\w)\1\1+", r"\1\1", word)


class SpellCheck:
    """A class that looks into the dictionary and checks for word suggestions for the inputted word"""

    def __init__(self, words, in_word):
        self.input_word = in_word
        self.words = words
        self.suggested_words = {}

    # look at words of similar length to the input word
    def __compute_suggested_words(self):
        if len(self.suggested_words) != 0:
            return
        for word in self.words:
            if len(self.input_word) == len(word):
                self.suggested_words[word] = self.__compute_count(word)

    # count how many alphabets of the input word is in each word in the dictionary
    def __compute_count(self, word):
        count = 0
        for i in range(len(self.input_word)):
            if self.input_word[i] in word:
                count += 1
        return count

    # find the most likely word that has been misspelled as the input word, using count and the length
    def find_likely_words(self):
        self.__compute_suggested_words()
        return [key for key, value in self.suggested_words.items() if value == len(self.input_word)]

    # find the nearest options to the most likely word
    def find_optional_words(self):
        self.__compute_suggested_words()
        return [key for key, value in self.suggested_words.items() if value == len(self.input_word) - 1]

# get input word


def ask():
    i_word = input("Word to check: ").lower()

    # clean the input of redundant triple dupes
    return erase_triple_dupes(i_word)

# check the input word against the dictionary of words and if it is a valid word, say so. Else use all the above methods to check for the nearest word to it and display those


def spell_checker(words):
    """look at input word and check if it is a valid English word as per our limited dictionary, or not. If invalid, make suggestions of similar words"""
    in_word = ask()
    print("The word you have asked to check is: " + in_word)

    if in_word in words:
        print("Yes it is a valid word")
    else:
        speller = SpellCheck(words, in_word)
        print("The word you are looking for maybe: ",
              speller.find_likely_words())
        if len(speller.find_likely_words()) == 0:
            print("Options: ",  speller.find_optional_words())


spell_checker(get_words())


import re

# open words.txt file which has about 1,000 commonly used words


def get_words():
    words = []
    with open("words.txt") as new_file:
        for word in new_file.readlines():
            word = word.strip()
            words.append(word)
        return words

# check for third consecutive duplicate letter in input and remove it as an autofix (English doesn't have any word with three consecutive duplicates)


def erase_triple_dupes(word):
    regex = re.compile(r"(.)\1\1+")
    return regex.sub(r"\1\1", word)


def compute_suggested_words(in_word, words):
    suggested_words = {}
    for word in words:
        if len(in_word) == len(word):
            suggested_words[word] = compute_count(in_word, word)
    return suggested_words


def compute_count(in_word, word):
    count = 0
    for i in range(len(in_word)):
        if in_word[i] in word:
            count += 1
    return count


def find_likely_words(count, in_word):
    return [key for key, value in count.items() if value == len(in_word)]


def find_optional_words(count, in_word):
    return [key for key, value in count.items() if value == len(in_word) - 1]


def ask():
    i_word = input("Word to check: ").lower()
    # clean the input of redundant triple dupes
    return erase_triple_dupes(i_word)


def spell_checker(words):
    """look at input word and check if it is a valid English word as per our limited dictionary, or not. If invalid, make suggestions of similar words"""
    # get input
    in_word = ask()
    print("The word you have asked to check is: " + in_word)
    if in_word in words:
        print("Yes it is a valid word")
    # if the word does not match any in our dictionary, suggest alternatives
    else:
        count = compute_suggested_words(in_word, words)
        print("This maybe the word you are looking for: ",
              find_likely_words(count, in_word))
        print("Options: ",  find_optional_words(count, in_word))


spell_checker(get_words())


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


def spell_checker(words):
    """look at input word and check if it is a valid English word as per our limited dictionary, or not. If invalid, make suggestions of similar words"""

    # get input
    i_word = input("Word to check: ").lower()
    # clean the input of redundant triple dupes
    in_word = erase_triple_dupes(i_word)
    print("The word you have asked to check is: " + in_word)

    # check the word against the dictionary in our txt file
    suggest_words = []
    if in_word in words:
        print("Yes it is a valid word")
    # if the word does not match any in our dictionary, suggest alternatives
    else:
        for word in words:
            if len(in_word) == len(word):
                for i in range(len(in_word)):
                    if in_word[i] in word:
                        # get all words that have the input alphabets in them
                        suggest_words.append(word)

        count = {}
        suggest_arr = []
        word_arr = []
        for word in suggest_words:
            # get the count of each word that is suggested. For the correct word, the count will be the same as the length of the word,as each iteration would have added that word to suggest_words list
            count[word] = suggest_words.count(word)

        for key, value in count.items():
            if value == len(in_word):
                word_arr.append(key)
            if value == (len(in_word))-1:
                suggest_arr.append(key)
        print("This maybe the word you are looking for: ", word_arr)
        print("Options: ",  suggest_arr)


spell_checker(get_words())

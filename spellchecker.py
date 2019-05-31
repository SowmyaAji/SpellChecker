

# open words.txt file which has about a 1,000 commonly used words

words = []
with open("words.txt") as new_file:
    for word in new_file.readlines():
        word = word.strip()
        words.append(word)


def spell_checker(words):
    """look at input word and check if it is valid or not. If invalid, make suggestions of similar words"""

    suggest_words = []
    # get input
    i_word = input("Word to check: ").lower()
    if i_word in words:
        print("Yes it is a valid word")
    else:

        for word in words:
            if len(i_word) == len(word):
                for i in range(len(i_word)):
                    if i_word[i] in word:
                        # get all words that have the input alphabets in them
                        suggest_words.append(word)

        count = {}
        suggest_arr = []
        word_arr = []
        for word in suggest_words:
            # get the count of each word that is suggested. For the correct word, the count will be the same as the length of the word,as each iteration would have added that word to suggest_words list
            count[word] = suggest_words.count(word)

        for key, value in count.items():
            if value == len(i_word):
                word_arr.append(key)
            if value == (len(i_word))-1:
                suggest_arr.append(key)
        print("This maybe the word you are looking for: ", word_arr)
        print("Options: ",  suggest_arr)


spell_checker(words)

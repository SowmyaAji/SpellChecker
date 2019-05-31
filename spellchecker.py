# from spellchecker import SpellChecker

words = []
with open("words.txt") as new_file:
    for word in new_file.readlines():
        word = word.strip()
        words.append(word)


def spell_checker(words):
    # spell = SpellChecker()
    suggest_words = []
    i_word = input("Word to check: ").lower()
    if i_word in words:
        print("Yes it is a valid word")
    else:
        # print(spell.correction(i_word))
        # print(spell.candidates(i_word))
        for word in words:
            if len(i_word) == len(word):
                for i in range(len(i_word)):
                    if i_word[i] in word:
                        suggest_words.append(word)
        count = {}
        suggest_arr = []
        word_arr = []
        for word in suggest_words:
            count[word] = suggest_words.count(word)

        for key, value in count.items():
            if value == len(i_word):
                word_arr.append(key)
            if value == (len(i_word))-1:
                suggest_arr.append(key)
        print("This maybe the word you are looking for: ", word_arr)
        print("Options: ",  suggest_arr)


spell_checker(words)

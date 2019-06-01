# SpellChecker


#Overview

A python program to check if a word has been misspelt. This is an attempt
to work it out without using the python library pyspellchecker which does
the job quite efficiently. There is also the http://norvig.com/spell-correct.html 
solution and the Javascript version of it:
https://github.com/WillSen/spellchecker-autocorrect/blob/master/index.js
both of which are fuller solutions

#Installation

Clone this repository, cd into it and run python spellchecker.py from command line


##Input

Check if a word exists in the dictionary. 

'apple'

##Output

'That is a valid word'

##Input

Where the word is misspelt by a letter set in a different place

'abel'

##Output


Suggestion word with transposed letters

('This maybe the word you are looking for: ', ['able'])

Additional suggestions, in case it is not just a problem of transposed letters

('Options: ', ['late', 'real', 'beat', 'deal', 'blue', 'lead', 'base', 'ball'])

##Input

Where the word is misspelt by a letter set in a different place, with a duplicate letter

'appel'

##Output


If an alphabet is repeated, the program  tries to find another word with another alphabet
that could be in place of the repeatedalphabet. It also suggests the word with transposed letters.

('This maybe the word you are looking for: ', ['place', 'apple'])

Valid options with just one alphabet or two alphabets that are different:

('Options: ', ['paper', 'plant', 'space', 'apply', 'speak', 'peace'])

##Input

Where the word does not exist in the dictionary used:

'arl'

##Output

The program finds the optional words that it thinks the word may be:

('This maybe the word you are looking for: ', [])

('Options: ', ['all', 'art', 'arm', 'war', 'far', 'lay', 'law', 'bar', 'car', 'air'])


#Input

Excess letters

'happpy'

#Output

The program automatically removes the third consecutive duplicate letter, as English does not have a 
single word with three consecutive duplicates - like 'ppp' in the example given. Our program cleans up that
input by removing the third duplicate and returns it as a valid word.

Word to check: 'happpy'

The word you have asked to check is: happy [this is the auto-corrected result]

Yes it is a valid word

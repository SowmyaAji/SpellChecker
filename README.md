# SpellChecker


#Overview

A python formula to check if a word has been misspelt. This is an attempt
to work it out without using the python library pyspellchecker which does
the job quite efficiently. There is also the http://norvig.com/spell-correct.html 
solution and the Javascript version of it:
https://github.com/WillSen/spellchecker-autocorrect/blob/master/index.js
both of which are fuller solutions

#Input

Check if a word exists in the dictionary. 
'apple'

#Output

'That is a valid word'

#Input
Where the word is misspelt by a letter set in a different place
'abel'

#Output
Suggestion word with transposed letters
('This maybe the word you are looking for: ', ['able'])
('Options: ', ['late', 'real', 'beat', 'deal', 'blue', 'lead', 'base', 'ball'])

#Input
Where the word is misspelt by a letter set in a different place, with a duplicate letter
'appel'

#Output
If an alphabet is repeated, the program 
tries to find another word with another alphabet that could be in place of the repeated
alphabet. It also suggests the same word with transposed letters.

('This maybe the word you are looking for: ', ['place', 'apple'])
('Options: ', ['paper', 'plant', 'space', 'apply', 'speak', 'peace'])

#Input
Where the word does not exist in the dictionary used
'arl'

#Output
The program finds the optional words that it thinks the word may be
('This maybe the word you are looking for: ', [])
('Options: ', ['all', 'art', 'arm', 'war', 'far', 'lay', 'law', 'bar', 'car', 'air'])


#Input
Excess letters
'happpy'

#Output
The program does not account for excess letters, it returns words that could have some of those 
letters and are of the same length.

('This maybe the word you are looking for: ', [])
('Options: ', ['happen', 'player'])

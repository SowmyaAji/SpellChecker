# SpellChecker


#Overview

A python formula to check if a word has been misspelt. This is an attempt
to work it out without using the python library pyspellchecker which does
the job quite efficiently. There is also the http://norvig.com/spell-correct.html 
solution and the Javascript version of it:
https://github.com/WillSen/spellchecker-autocorrect/blob/master/index.js
both of which are fuller solutions

##Input

Check if a word exists in the dictionary. 
'apple'

##Output

'That is a valid word'

##Input
Where the word is misspelt by a letter set in a different place
'abel'

##Output
Suggestion word with transposed letters<br>
('This maybe the word you are looking for: ', ['able'])

Additional suggestions, in case it is not just a problem of transposed letters<br>


('Options: ', ['late', 'real', 'beat', 'deal', 'blue', 'lead', 'base', 'ball'])<br>

##Input
Where the word is misspelt by a letter set in a different place, with a duplicate letter<br>
'appel'

##Output
If an alphabet is repeated, the program  tries to find another word with another alphabet
that could be in place of the repeatedalphabet. It also suggests the word with transposed letters.<br>

('This maybe the word you are looking for: ', ['place', 'apple'])

Valid options with just one alphabet or two alphabets that are different:<br>


('Options: ', ['paper', 'plant', 'space', 'apply', 'speak', 'peace'])

##Input
Where the word does not exist in the dictionary used:<br>
'arl'

##Output
The program finds the optional words that it thinks the word may be:<br>
('This maybe the word you are looking for: ', [])
('Options: ', ['all', 'art', 'arm', 'war', 'far', 'lay', 'law', 'bar', 'car', 'air'])


#Input
Excess letters<br>
'happpy'

#Output
The program does not account for excess letters, it returns words that could have some of those 
letters and are of the same length.<br>

('This maybe the word you are looking for: ', [])
('Options: ', ['happen', 'player'])

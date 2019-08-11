# SpellChecker


## Overview

A python program to check if a word has been misspelt. This is an attempt to work it out without using the python library pyspellchecker which does
the job quite efficiently.

I have it in the pip file and it will get installed if you use the requirements.txt I have listed below. The code to use pyspellchecker, however, is not listed in this repository. You can write it on your own if you wish. The examples and docs are here:
https://pypi.org/project/pyspellchecker/

There is also the http://norvig.com/spell-correct.html 
solution and the Javascript version of it:
https://github.com/WillSen/spellchecker-autocorrect/blob/master/index.js both of which are fuller solutions that the one I have written, which is much simpler and easier.

## Installation

Project requires python 3.6.8 and pip 19.1.1


Clone this repository, cd into it. And run from command line:

```
$ pipenv shell
$ pip install -r requirements.txt
$ python spellchecker.py 
```

### Input

Check if a word exists in the dictionary. 

```
Word to check: 'apple'
```

### Output

```
The word you have asked to check is: apple
Yes it is a valid word

```

### Input

Where the word is misspelt by a letter set in a different place

```
Word to check: 'abel'

```

### Output

```
The word you have asked to check is: abel
('The word you are looking for maybe: ', ['blae', 'able', 'bale'])

```
### Input

Where the word is misspelt by a letter set in a different place, with a duplicate letter

```
Word to check: 'appel'
```

### Output


If an alphabet is repeated, the program  tries to find another word with another alphabet
that could be in place of the repeated alphabet. It also suggests the word with transposed letters.

The word you have asked to check is: appel
('The word you are looking for maybe: ' ['panel', 'plate', 'palce', 'lampe', 'pearl', 'plena', 'sepal', 'place', 'plage', 'penal', 'aleph', 'plane', 'plead', 'pleas', 'maple', 'petal', 'leaps', 'lepas', 'nepal', 'pleat', 'apple', 'lapse', 'pedal', 'ample', 'lapel', 'pilea'])

### Input

Where the word does not exist in the dictionary used:

```
Word to check:'arl'
```

### Output

The program finds the optional words that it thinks the word may be:

```
The word you have asked to check is: arl
('The word you are looking for maybe: ', [])
('Options: ', ['all', 'ale', 'alb', 'ala', 'alt', 'als', 'alp', 'far', 'lea', 'bra', 'ora', 'ayr', 'car', 'tar', 'lao', 'lad', 'lag', 'lab', 'lac', 'lax', 'lay', 'lat', 'law', 'lap', 'mal', 'rya', 'dal', 'mar', 'asl', 'val', 'las', 'rag', 'rad', 'sal', 'rao', 'ram', 'raj', 'rah', 'rat', 'rap', 'sar', 'ray', 'lir', 'kal', 'awl', 'jar', 'bar', 'bal', 'ars', 'art', 'ara', 'arc', 'are', 'ark', 'arm', 'ira', 'era', 'raw', 'gar', 'gal', 'air', 'ail', 'par', 'pal', 'ola', 'war', 'ear', 'oar'])

```

### Input

Excess letters

```
Word to check: 'happpy'

```

### Output

The program automatically removes the third consecutive duplicate letter, as English does not have a single word with three consecutive duplicates - like 'ppp' in the example given. Our program cleans up that
input by removing the third duplicate and returns it as a valid word.

```
The word you have asked to check is: happy 
```
[this is the auto-corrected result]

```
Yes it is a valid word
```


## Testing

I've also written three simple pytests for this program. To run the tests:

```
pytest test_spellchecker.py

```

### Output

```

============================= test session starts ==============================
platform darwin -- Python 3.6.8, pytest-4.6.1, py-1.8.0, pluggy-0.12.0
rootdir: /Users/sowmya/spellchecker-python
collected 3 items

test_spellchecker.py ...                                                 [100%]

=========================== 3 passed in 0.03 seconds ===========================

```

# CNLP
![](https://img.shields.io/badge/Python-3.8.10-blue)
![](https://img.shields.io/badge/Spacy-3.4.3-ff69b4)

CNLP is aset of text processing tools with different NLP (Natural Language Processing) techniques.

<br/>

## Installation et configuration

### Install python3 

```sh
sudo apt install python3;\
sudo apt install python3-pip
```

You have to make sure of the version of python that is installed. The version of python
used is `python 3.8.10`.


### Install venv
```sh
sudo apt install python3-venv
```
OU
```sh
sudo pip3 install virtualenv
```

### Create virtual environment
```sh
python3 -m venv env
```
OU
```sh
virtualenv env -p python3
```

### Lauch environment
```sh
source env/bin/activate
```

## Python version

```sh
python --version
```

Show :

```
Python 3.8.10
```


### Installing of dependancies
1. Install the requirements.txt content.

```sh
pip install -r requirements.txt
```

## Usage
1. Create a text file named `en_text_file.txt` in project root and put the following text for example:

```
Grammar is without a doubt one of the most daunting aspects of the English
language, an area riddled with complexities, inconsistencies, and contradictions.
It has also been in a state of flux for pretty much its entire existence. For native
speakers of English, as well as for those learning it as a new language, grammar
presents a very serious challenge to speaking and writing both accurately and
effectively.
Having a single, reliable, go-to reference guide should therefore be indispensable
to those trying to learn, improve, or perfect their speech or writing. This book is
that guide: a clear, unambiguous, and comprehensive source of information that
covers all the relevant topics of English grammar, while still being easy to
understand and enjoyable to read.
Every topic in the book has been broken down into basic units. Each unit can be
read and understood in its own right, but throughout the book you will find
cross-references to other sections and chapters to help make it clear how all the
pieces fit together. If you’re having trouble understanding something, try going
back (or forward) to other related topics in the book.
Finally, it must be mentioned that, because English is such a flexible,
inconsistent language, the “rules” that are often bandied about are usually not
rules at all, but rather guides that reflect how the language is used. Accordingly,
the guidelines contained within this book are just that—guidelines. They are not
intended to provide constrictive or proscriptive rules that confine everyone to a
particular way of speaking or writing.
Learning how the English language works will enhance your engagement with
speech and writing every day, from the books you read, to the e-mails you write,
to the conversations you have with friends and strangers alike.
As such, mastering grammar is not an exercise that is confined to the classroom.
While it is certainly important to learn the structures, styles, and rules that shape
the language, the key to truly learning English is to read and listen to the way
people write and speak every day, from the most well-known authors to the
people you talk to on the bus. Take the information you find in this book and
carry it with you into the world.

```

2. Create a python module named `main.py` in root project and write the following code into it.

```python
from cnlp import GSET as settings  # Importation of config variable.
from cnlp.texumer import RlvSent
"""Importation of algorithm of extraction of relevant sentences from a text."""


# we set the language of the NLP processing in English, in this cas.
settings['LANGUAGE_PROCESSED'] = 'EN'

with open('en_text_file.txt', 'r', encoding='utf-8') as f:
    text = f.read()  # open file and read the text content.
    algo = RlvSent()  # initialize the algorithm.
    res  = algo(text)  # apply a traitment on the text.
    
    # we show the results
    print("\n{} results found.".format(len(res)))
    print(' '.join(res))


```

3. Execute this python module.

```sh
python main.py
```

Execution results:

```
[12:34:39 516ms MainThread] Loading and configuration pre-trainned model of the language processed...
[12:34:40 476ms MainThread] Matching of the text to sentences ...
15 sentences found.
[12:34:40 539ms MainThread] Calculation of TF-IDF for each word contained into sentences...

...

[12:34:40 544ms MainThread] Executed in 1.028sec.

4 results found.
For native speakers of English, as well as for those learning it as a new language, 
grammar presents a very serious challenge to speaking and writing both accurately and effectively. 
This book is that guide: a clear, unambiguous, and comprehensive source of information 
that covers all the relevant topics of English grammar, while still being easy to 
understand and enjoyable to read. Learning how the English language works will enhance 
your engagement with speech and writing every day, from the books you read, to the e-mails 
you write, to the conversations you have with friends and strangers alike. While it is certainly 
important to learn the structures, styles, and rules that shape the language, the key to 
truly learning English is to read and listen to the way people write and speak every day, 
from the most well-known authors to the people you talk to on the bus.

```

From 15 sentences, we have got 4 sentences for the summary. :)


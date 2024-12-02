import nltk
import pymorphy3
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

file = open(r'textfile.txt', encoding='utf-8')
text = file.read()

tokenized_text = word_tokenize(text)

marks = ('.', ',', '!', '?', '(', ')', ':', ';','—','...')
tokens = list(t for t in tokenized_text if t not in marks)

pairs = list(zip(tokens, tokens[1:]))
pyma = pymorphy3.MorphAnalyzer()

for (current_word, next_word) in pairs:
    current_word = pyma.parse(current_word)[0]
    next_word =  pyma.parse(next_word)[0]
    if current_word.tag.POS not in ('NOUN', 'ADJF', 'ADJS'): continue
    if next_word.tag.POS not in ('NOUN', 'ADJF', 'ADJS'): continue
    if current_word.tag.gender == next_word.tag.gender and current_word.tag.number == next_word.tag.number and current_word.tag.case == next_word.tag.case:
        print(current_word.word, next_word.word)
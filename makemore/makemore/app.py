import sys

from makemore.word_set import WordSet
from makemore.bigram import BigramSet

if __name__ == "__main__":
    ws = WordSet().load("names.txt")
    b = BigramSet()
    b.add_words(ws.words)

    b.normalize().bigrams  

    noise = 0.0

    n = b.next_char('^', noise)

    while n != '$':
       print(n, end='')
       n = b.next_char(n, noise)
    print()


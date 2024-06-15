import random

class BigramSet:
    def __init__(self):
        self.bigrams = dict()
    
    def add_word(self, word):
        for c1, c2 in zip(word, word[1:]):
            if c1 not in self.bigrams:
                self.bigrams[c1] = dict()
            if c2 not in self.bigrams[c1]:
                self.bigrams[c1][c2] = 0
            self.bigrams[c1][c2] += 1
        return self
    
    def add_words(self, words):
        for word in words:
            self.add_word(word)
        return self
    
    def normalize(self):
        for c1 in self.bigrams:
            total = sum(self.bigrams[c1].values())
            for c2 in self.bigrams[c1]:
                self.bigrams[c1][c2] /= total
                self.bigrams[c1][c2] += 0.0000000000000001
        return self
    
    def next_char(self, c1, noise=0.0):
        if c1 not in self.bigrams:
            return None
        r = random.random() + noise
        for c in self.bigrams[c1]:
            if r < self.bigrams[c1][c]:
                return c
            r -= self.bigrams[c1][c]
        return '$'


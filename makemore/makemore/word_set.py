class WordSet:

    def __init__(self):
        self.words = []
    
    def load(self, path):
        with open(path, 'r') as f:
            for line in f:
                self.words.append(f"^{ line.strip().lower() }$")
        return self
    
    def __iter__(self):
        return iter(self.words)
    

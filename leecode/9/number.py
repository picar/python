class Number:
    def __init__(self, x):
        self.x = x

    def is_palindrome_str(self):
        return str(self.x) == str(self.x)[::-1]
    
    def is_palindrome(self):
        if self.x < 0:
            return False
        x, y = self.x, 0
        while x > 0:
            y = y * 10 + x % 10
            x = x // 10
        return self.x == y
    
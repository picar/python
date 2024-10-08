class RomanNumber:
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    def __init__(self, n: str):
        self.n = n
    
    def __int__(self) -> int:
        v, i = 0, 0
        while i < len(self.n):
            if self.n[i:i+2] in RomanNumber.values:
                v += RomanNumber.values[self.n[i:i+2]]
                i += 1
            else:
                v += RomanNumber.values[self.n[i]]
            i += 1
        return v

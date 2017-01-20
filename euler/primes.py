#!/usr/bin/env python3

from sys import argv

class Primes(object):

    def __init__(self):
        self._primes = []
        self._generator = self._prime_generator()

    def reset(self):
        self._generator = self._prime_generator()
        return self

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._generator)

    def _is_prime(self, num):
        if num in self._primes:
             return True
        for p in self._primes:
            if not num % p:
                return False
            if p > num:
                return True
        return True
 
    def _prime_generator(self):
        x = 2
        while True:
            if self._is_prime(x):
                if x not in self._primes:
                    self._primes.append(x)
                yield x
            x += 1

def prime_factor(primes, num):
    if type(num) == type(1):
        num = [ (1,1,num) ]
    last = num[-1][2]
    while True:
        prime=next(primes)
        if not last % prime:
            num.append((last, prime, int(last/prime)))
            return prime_factor(primes, num)
        if last == 1:
            break
        if prime > last:
            primes.reset()
            return prime_factor(primes, num)
    return num

def main():
    if len(argv) != 2:
        print("Usage: {} <integer>".format(argv[0]))
        return

    arg = int(argv[1])

    primes = Primes()

    factor_list=prime_factor(primes, arg)
    print([x[1] for x in factor_list if x[1] != 1])

if __name__ == '__main__':
    main()
    

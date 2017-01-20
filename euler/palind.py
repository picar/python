#!/usr/bin/env python3

from sys import argv

from primes import Primes, prime_factor

p=Primes()

c=999
for i in range(int(argv[1])): 
    n = int(str(c)+str(c)[::-1])
    p.reset()
    factor_list=prime_factor(p, n)
    print(n, [x[1] for x in factor_list if x[1] != 1])
    c-=1

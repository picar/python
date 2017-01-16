#!/usr/bin/env python3

from sys import argv

def fib(max):
    n, np1 = 0, 1
    while np1 < max:
        n, np1 = np1, n+np1
        yield n
    return 

def main():
    if len(argv) != 2: return
    for i in fib(int(argv[1])):
        print(i)
    return

if __name__ == '__main__':
    main()

 

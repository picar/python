#!/usr/bin/env python3

from sys import argv

print(sum([ x for x in range(int(argv[1])) if not x%3 or not x%5 ]))

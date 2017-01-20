#!/usr/bin/env python3

from sys import argv
from fib_enum import fib

print(sum([ x for x in fib(4000000) if not x%2 ]))

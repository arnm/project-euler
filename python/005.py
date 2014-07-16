# /usr/bin/env/ python

# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

from itertools import count

def is_evenly_divisible_by_range(n, range):
  for i in range:
    if n % i != 0: return False
  return True

def solve():
  for n in count(1):
    if is_evenly_divisible_by_range(n, range(1, 21)): return n

if __name__ == '__main__': solve()

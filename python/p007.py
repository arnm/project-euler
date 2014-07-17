# /usr/bin/env/ python

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.

# What is the 10,001st prime number?

from p003 import is_prime, primes
from itertools import islice

def solve():
  n = 10001
  return next(islice(primes(), n-1, n))

if __name__ == '__main__': print('Answer:', solve())

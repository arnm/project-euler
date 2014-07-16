# /usr/bin/env/ python

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

from itertools import count

def is_prime(n):
  if n <= 1: return False
  for i in range(2, n + 1):
    if n % i == 0 and i != n: return False
  return True

def primes():
  for n in count(start=2):
    if is_prime(n): yield n

def is_prime_factor(n, p):
  if not is_prime(p): return False
  return n % p == 0

def prime_factorize(n):
  if is_prime(n): return (n,)
  for p in primes():
    if is_prime_factor(n, p):
      return (p,) + prime_factorize(n // p)

def solve():
  prime_factors = prime_factorize(600851475143)
  print('Answer:', max(prime_factors))

if __name__ == '__main__': solve()

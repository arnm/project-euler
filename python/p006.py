# /usr/bin/env/ python

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025

# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

def solve():
  sum_squares = sum(map(lambda x: pow(x, 2), range(1, 101)))
  square_sum = pow(sum(range(1, 101)), 2)
  return square_sum - sum_squares

if __name__ == '__main__': print('Answer:', solve())

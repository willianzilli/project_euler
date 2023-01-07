# https://projecteuler.net/problem=3
# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
n = 600851475143
p = 2

while n >= (p * p):
    if n % p == 0:
        n = n // p

    p += 1

print(n)
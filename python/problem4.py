# https://projecteuler.net/problem=4
# Largest palindrome product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
import time
start_time = time.time()

x = 999
y = 999

max = 0

px = 0
py = 0

while True:
    p = x * y

    if (str(p) == str(p)[::-1] and p % 11 == 0 and max < p):
        max = p

    x -= 1

    if (x <= 100):
        x = 999
        y -= 1

        if (y <= 100):
            break

print("--- %s seconds ---" % (time.time() - start_time))
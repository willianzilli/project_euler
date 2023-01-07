# https://projecteuler.net/problem=5
# Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def res1():
    N = n = 20
    while True:
        all = N

        for i in range(1, N + 1):
            if (n % i != 0):
                n += 1
                break
            else:
                all -= 1

        if (all == 0):
            break

    print(n)

def res2():
    def _gcd(x, y):
        while x != y:
            if x > y:
                x = x - y
            else:
                y = y - x

        return x

    listOfNumbers = range(1, 20)
    res = listOfNumbers[0]
    for i in range(0, len(listOfNumbers)):
        num = listOfNumbers[i]

        gcd = _gcd(num, res)
        res = (res * num) // gcd

    print(res)

res2()
# CSCI 220/620
# Summer 2022
# Assignment 3 - Induction and Recursion
# James Post
import math
import itertools
import random


def find_postage(amount):
    four_stamps = 0
    five_stamps = 0
    while amount > 3:
        if amount % 4 == 0:
            four_stamps = amount/4
            return [four_stamps, 0]
        elif amount % 5 == 0:
            five_stamps = amount/5
            return [0, five_stamps]
        elif amount < 4 or amount == 6 or amount == 7 or amount == 11:
            return "N/A"
        while amount % 4 != 0:
            amount = amount - 5
            five_stamps += 1
        four_stamps = amount/4
        return [four_stamps, five_stamps]
    return "N/A"


def fib_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


def fib_formula(n):
    return int(1/math.sqrt(5)*(((1+math.sqrt(5))/2)**n-((1-math.sqrt(5))/2)**n))


def gcd_recursive(a, b):
    if a == 0:
        return b
    else:
        return gcd_recursive(b % a, a)


# modified from https://stackoverflow.com/questions/43119744/python-generate-all-possible-strings-of-length-n
def all_strings(alphabet, size):
    while size > 0:
        print([''.join(x) for x in itertools.product(alphabet, repeat=size)])
        size -= 1


def main():
    trials = 10
    for trial in range(trials):
        amount = random.randint(1, 100)
        print("Postage for", amount, "is", find_postage(amount))
    numbers = 10
    for n in range(2, numbers + 1):
        fr = fib_recursive(n)
        ff = fib_formula(n)
        print(n, "Fib. number recursive", fr, "formula", ff, "MATCH" if fr == ff else "ERROR")
    trials = 10
    for trial in range(trials):
        i = random.randint(1, 100)
        r = random.randint(1, 100)
        gr = gcd_recursive(i, r)
        gg = math.gcd(i, r)
        print("GCD Recursive", gr, "GCD built-in", gg, "MATCH" if gr == gg else "ERROR",)
    all_strings(['a'], 10)
    all_strings(['a', 'b', 'c'], 3)


if __name__ == "__main__":
    main()

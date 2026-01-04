#!/bin/python3

"""
Task
Given an integer, n, perform the following conditional actions:

* If n is odd, print Weird
* If n is even and in the inclusive range of 2 to 5, print Not Weird
* If n is even and in the inclusive range of 6 to 20, print Weird
* If n is even and greater than 20, print Not Weird

Input Format
A single line containing a positive integer, n.

Constraints
1 <= n <= 100

Output Format
Print Weird if the number is weird. Otherwise, print Not Weird.
"""

def check_weirdness(n):
    if n % 2 != 0:
        return "Weird"
    else:
        if n in range(2, 6):
            return "Not Weird"
        elif n in range(6, 21):
            return "Weird"
        elif n > 20:
            return "Not Weird"

if __name__ == '__main__':
    n = int(input("Digite um número: ").strip())
    result = check_weirdness(n)
    print(result)
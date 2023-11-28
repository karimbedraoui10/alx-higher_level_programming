#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_dgt = number % 10
if l_dgt == 0:
    print(f"Last digit of {number:d} is {l_dgt:d} and is 0")
elif l_dgt > 5:
    print(f"Last digit of {number:d} is {l_dgt:d} and is greater than 5")
else:
    print(f"Last digit of {number:d} is {l_dgt:d} and is less than 6 and not 0")

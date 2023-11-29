#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        if n % 3 == 0:
            if n / 3 == 5:
                print("FizzBuzz", end=" ")
            else:
                print("Fizz", end=" ")
        elif n % 5 == 0:
            if n / 5 == 3:
                print("FizzBuzz", end=" ")
            else:
                print("Buzz", end=" ")
        else:
            print("{:d}".format(n), end=" ")

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0 or number == 0:
    Last_dig = number % 10
elif number < 0:
    Last_dig = number % -10
if Last_dig > 5:
    print(f"Last digit of {number} is {Last_dig} and is greater than 5")
elif Last_dig == 0:
    print(f"Last digit of {number} is {Last_dig} and is 0")
else:
    print(f"Last digit of {number} is {Last_dig} and is less than 6 and not 0")

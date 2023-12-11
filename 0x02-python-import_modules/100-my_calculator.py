#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ != "__main__":
    exit()

number = len(argv) - 1
if number != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

elif argv[2] == '+':
    func = add
elif argv[2] == '-':
    func = sub
elif argv[2] == '*':
    func = mul
elif argv[2] == '/':
    func = div
else:
    print("Unknown operator. Available operators: +, -, *, and /")
    exit(1)

result = func(int(argv[1]), int(argv[3]))
print("{:d} {:s} {:d} = {:d}".format(int(argv[1]),
    argv[2], int(argv[3]), result))

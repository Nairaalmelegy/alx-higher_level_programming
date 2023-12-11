#!/usr/bin/python3
import sys
if __name__ != "__main__":
    exit()

i = len(sys.argv) - 1
if i == 0:
    print("{:d} arguments.".format(i))
elif i > 0:
    if i == 1:
        for arg in sys.argv:
            if i != 0:
                print("{:d}: {:s}".format(i, arg))
            i += 1
    elif i > 1:
        print("{:d} arguments:".format(i))
        for arg in sys.argv:
            if i != 0:
                print("{:d}: {:s}".format(i, arg))
            i += 1

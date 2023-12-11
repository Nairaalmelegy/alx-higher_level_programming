#!/usr/bin/python3
import sys
if __name__ != "__main__":
    exit()

i = len(sys.argv) - 1
if i == 0:
    print("{:d} arguments.".format(i))
elif i > 0:
    if i == 1:
        print("{:d} argument:".format(i))
        j = 0
        for arg in sys.argv:
            if j != 0:
                print("{:d}: {:s}".format(j, arg))
            j += 1
    elif i > 1:
        print("{:d} arguments:".format(i))
        j = 0
        for arg in sys.argv:
            if j != 0:
                print("{:d}: {:s}".format(j, arg))
            j += 1

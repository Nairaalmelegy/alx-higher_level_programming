#!/usr/bin/python3
import sys

if __name__ == "__main__":
    number = len(sys.argv) - 1
    i = 0
    sumi = 0
    for arg in sys.argv:
        if i != 0:
            sumi += int(arg)
        i += 1
    print("{:d}".format(sumi))

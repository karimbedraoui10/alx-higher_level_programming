#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    size = len(sys.argv) - 1
    if size == 0:
        print("0 arguments.")
    elif size == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(size))
    for n in range(1, size + 1):
        print("{}: {}".format(n, sys.argv[n]))


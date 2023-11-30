#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    size = len(sys.argv) - 1
    r = 0
    for n in range(size):
        i = int(sys.argv[n + 1])
        r = r + i
    print("{}".format(r))

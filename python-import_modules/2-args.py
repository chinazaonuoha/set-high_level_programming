#!/usr/bin/env python3


if __name__ == "__main__":
    import sys
    list_args = sys.argv[1:]
    for i, arg in enumerate(list_args, start=1):
        print(" {}: {}".format(i, arg))
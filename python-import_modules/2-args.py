#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    list_args = sys.argv[1:]
    num_args = len(list_args)

    if num_args == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(num_args, "" if num_args == 1 else "s"))

    for i, arg in enumerate(list_args, start=1):
        print("{}: {}".format(i, arg))

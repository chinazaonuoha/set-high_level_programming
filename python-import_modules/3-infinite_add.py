#!/usr/bin/env python3
import sys


def add_arguments():
    list_args = sys.argv[1:]
    total = sum(int(arg) for arg in list_args)
    print(total)


if __name__ == "__main__":
    add_arguments()

#!/usr/bin/python3
def print_alphabet():
    print(*map(chr, range(65, 91)), sep=str())

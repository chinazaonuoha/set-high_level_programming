#!/usr/bin/python3


def print_comb2():
    for i in range(100):
        print(
            "{:02d}".format(i),
            end="\n" if i == 99 else ", ",
        )


print_comb2()

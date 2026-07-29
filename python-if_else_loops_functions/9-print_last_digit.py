#!/usr/bin/python3


def print_last_digit(number):
    BASE_TEN_DIVISOR = 10
    last_digit = (
        -number % BASE_TEN_DIVISOR
        if number < 0
        else number % BASE_TEN_DIVISOR
    )
    print("{}".format(last_digit), end="")
    return last_digit

#!/usr/bin/env python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    ops = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }


    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, b = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])

    if operator not in ops:
        print("Unknown operator. Only: +, -, * and / available")
        sys.exit(1)

    result = ops[operator](a, b)
    print(f"{a} {operator} {b} = {result}")

#!/usr/bin/python3

excluded = {'e', 'q'}

output = "".join(
    chr(code) for code in range(ord('a'), 123)
    if chr(code) not in excluded
)
print("{:s}".format(output), end="")

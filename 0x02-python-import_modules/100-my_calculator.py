#!/usr/bin/python3

import sys

if __name__ == "__main__":

    """Func for basic math operations but with exceptions"""

    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = int(sys.argv[2])
    b = int(sys.agv[3])
    result = None

    if operator == "+":
        add(a, b)
    if operator == "-":
        sub(a, b)
    if operator == "*":
        mul(a, b)
    if operator == "/":
        div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print(f"{a} {operator} {b} {result}")

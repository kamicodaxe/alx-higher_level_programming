#!/usr/bin/python3

def main():
    a = 10
    b = 5

    from calculator_1 import add, sub, mul, div

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))


if __name__ == "__main__":
    main()

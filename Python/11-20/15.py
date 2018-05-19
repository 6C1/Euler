import math


def f(x):
    return math.factorial(2 * x) // (math.factorial(x) ** 2)


if __name__ == '__main__':
    print(f(20))

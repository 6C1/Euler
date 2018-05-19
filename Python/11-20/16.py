import functools


def digit_sum(b, e):
    return sum(map(int, str(functools.reduce(
        lambda a, _: a * b,
        range(e),
        1,
    ))))


if __name__ == '__main__':
    print(digit_sum(2, 1000))

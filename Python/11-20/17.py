import os


def name(n):
    return {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred',
        1000: 'thousand',
    }.get(n, '')


def name_number(n):
    thousands = n // 1000
    thousand = bool(thousands)
    hundreds = (n % 1000) // 100
    hundred = bool(hundreds)
    tens, ones = (
        (n % 100, 0)
        if 10 < (n % 100) < 20
        else (((n % 100) // 10) * 10, n % 10)
    )
    and_h = 'and' if hundred and (tens or ones) else ''

    return [
        name(thousands),
        name(1000 if thousand else None),
        name(hundreds),
        name(100 if hundred else None),
        and_h,
        name(tens),
        name(ones),
    ]


def sum_names(upper_bound):
    return sum(
        sum(map(len, filter(bool, name_number(n))))
        for n in range(1, upper_bound + 1)
    )


def test():
    return all(
        name_number(i) == expected
        for i, expected in [
            (1, ['', '', '', '', '', '', 'one']),
            (5, ['', '', '', '', '', '', 'five']),
            (10, ['', '', '', '', '', 'ten', '']),
            (11, ['', '', '', '', '', 'eleven', '']),
            (19, ['', '', '', '', '', 'nineteen', '']),
            (20, ['', '', '', '', '', 'twenty', '']),
            (100, ['', '', 'one', 'hundred', '', '', '']),
            (101, ['', '', 'one', 'hundred', 'and', '', 'one']),
            (150, ['', '', 'one', 'hundred', 'and', 'fifty', '']),
            (999, ['', '', 'nine', 'hundred', 'and', 'ninety', 'nine']),
            (1000, ['one', 'thousand', '', '', '', '', '']),
        ]
    )


if __name__ == '__main__':
    print(test() if os.getenv('EULER_TEST') else sum_names(1000))

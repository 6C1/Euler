def longest_chain():
    max_key = 1
    upper_bound = 10 ** 6 - 1
    cache = {1: 1}
    for k in range(upper_bound, upper_bound // 2, -2):
        if k not in cache:
            a = [int(k)]
            while a[-1] not in cache:
                a += [(a[-1] // 2) if (a[-1] % 2 == 0) else (3 * a[-1] + 1)]
            for c, n in enumerate(a[::-1]):
                cache[n] = c + 1 + cache[a[-1]]
            if cache[k] > cache[max_key]:
                max_key = k
    print(max_key)


if __name__ == '__main__':
    longest_chain()

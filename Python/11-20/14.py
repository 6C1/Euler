import datetime

TAB = '\t'


class Collatz(dict):

    def __init__(self, *args, **kwargs):
        self.maxkey = 0
        super(Collatz, self).__init__(*args, **kwargs)
        self.update({0: 0, 1: 1})

    def __setitem__(self, key, item):
        if item > self.maxval:
            self.maxkey = key
        super(Collatz, self).__setitem__(key, item)

    def __getitem__(self, i):
        if i not in self:
            self[i] = self[self.collatz(i)] + 1
        return super(Collatz, self).__getitem__(i)

    @staticmethod
    def collatz(i):
        return (i // 2) if (i % 2 == 0) else (3 * i + 1)

    @property
    def maxval(self):
        return self[self.maxkey]

    @classmethod
    def main(cls, exp, verbose=False):
        now = datetime.datetime.utcnow()
        collatz = cls()
        upper_limit = 10 ** exp
        for i in range(1, upper_limit):
            if i not in collatz:
                _ = collatz[i]
                if verbose:
                    print(
                        len(collatz),
                        int(1000 * len(collatz) / i) / 1000,
                        TAB,
                        i,
                        TAB,
                        collatz[i],
                        TAB,
                        collatz.collatz(i),
                        collatz[collatz.collatz(i)],
                    )
        print(TAB, collatz.maxkey, collatz.maxval)
        duration = datetime.datetime.utcnow() - now
        print(TAB, duration, duration / upper_limit)


if __name__ == '__main__':
    for limit in range(1, 7):
        if limit:
            print('-' * 7)
        print('N =', limit)
        Collatz.main(limit)

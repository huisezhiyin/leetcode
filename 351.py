class Solution:
    def __init__(self):
        self.used = []

    def numberOfPatterns(self, m: int, n: int) -> int:
        res = 0
        lens = m
        for i in range(n - m + 1):
            res += self.calc_patterns(-1, lens)
            for j in range(9):
                self.used[j] = False
        return res

    def is_valid(self, index, last):
        if self.used[index]:
            return False
        if last == -1:
            return True
        if (index + last) % 2 == 1:
            return True
        mid = (index + last) // 2
        if mid == 4:
            return self.used[mid]
        if (index % 3 != last % 3) and (index / 3 != last / 3):
            return True
        return self.used[mid]

    def calc_patterns(self, last, lens):
        if lens == 0:
            return 1
        sums = 0
        for i in range(9):
            if self.is_valid(i, last):
                self.used[i] = True
                sums += self.calc_patterns(i, lens - 1)
                self.used[i] = False
        return sums

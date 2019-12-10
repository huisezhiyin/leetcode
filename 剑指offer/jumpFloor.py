# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        if number <= 2:
            return number
        result = 0
        n, m = 1, 2
        for i in range(number - 2):
            result = m + n
            n, m = m, result
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloor(4))

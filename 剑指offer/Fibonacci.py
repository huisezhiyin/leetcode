# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        if n in [0, 1]:
            return n
        s = 1
        one = 0
        for index in range(2, n + 1):
            s = s + one
            one = s - one
        return s


if __name__ == '__main__':
    s = Solution()
    print(s.Fibonacci(2))

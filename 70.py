class Solution:
    def climbStairs(self, n: int) -> int:
        tmp = {}
        tmp[0] = 0
        tmp[1] = 1
        tmp[2] = 2
        for i in range(3, n + 1):
            tmp[i] = tmp[i - 1] + tmp[i - 2]
        return tmp[n]

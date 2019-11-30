class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        # 从左往右最大的值
        row_maxes = [max(row) for row in grid]
        # 从上往下最大值
        col_maxes = [max(col) for col in zip(*grid)]
        s = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 迭代每一个元素 从上往下和从左往右里比较小的那个值 就是可以赋值的
                elm = grid[i][j]
                m = min(row_maxes[i], col_maxes[j])
                s += (m - elm)
        return s

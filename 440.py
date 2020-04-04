class Solution(object):
    def get_count(self, prefix, n):
        cur = prefix
        nex = prefix + 1
        count = 0
        while cur <= n:
            count += (min(n + 1, nex) - cur)
            cur *= 10
            nex *= 10
        return count

    def findKthNumber(self, n: int, k: int) -> int:
        p = 1
        prefix = 1
        while p < k:
            count = self.get_count(prefix, n)
            if (p + count) > k:  # 在这个前缀下 进入前缀子树 并且p切换到当前子节点
                prefix *= 10
                p += 1
            else:  # 不在这个前缀下 切换到下一个前缀 p切换到下一个前缀树的头部节点
                prefix += 1
                p += count
        return prefix

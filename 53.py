class Solution:
    def cross_sum(self, nums):
        ans = nums[0]
        sum_ = 0
        for num in nums:
            if sum_ > 0:
                sum_ += num
            else:
                sum_ = num
            ans = max(ans, sum_)
        return ans

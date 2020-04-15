class Solution:
    def twoSum(self, nums, target: int):
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        for j in range(len(nums)):
            if (target - nums[j] in d) and d[target - nums[j]] != j:
                return [j, d[target - nums[j]]]

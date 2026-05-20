class Solution:
    def twoSum(self, nums, target):
        d = {}

        for i, n in enumerate(nums):
            x = target - n

            if x in d:
                return [d[x], i]

            d[n] = i
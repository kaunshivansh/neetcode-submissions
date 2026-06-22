from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [x for x in nums if x > 0] + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for left in range(n - length):
                right = left + length

                best = 0
                for last in range(left + 1, right):
                    best = max(
                        best,
                        dp[left][last]
                        + dp[last][right]
                        + nums[left] * nums[last] * nums[right]
                    )

                dp[left][right] = best

        return dp[0][n - 1]
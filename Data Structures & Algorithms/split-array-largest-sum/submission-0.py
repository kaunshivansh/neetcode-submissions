class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def can_split(max_sum: int) -> bool:
            parts = 1
            current = 0

            for num in nums:
                if current + num > max_sum:
                    parts += 1
                    current = num

                    if parts > k:
                        return False
                else:
                    current += num

            return True

        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2

            if can_split(mid):
                right = mid
            else:
                left = mid + 1

        return left
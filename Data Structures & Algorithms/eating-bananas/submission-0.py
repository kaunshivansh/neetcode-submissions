class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            k = (left + right) // 2

            hours = 0

            for pile in piles:
                hours += (pile + k - 1) // k

            if hours <= h:
                right = k
            else:
                left = k + 1

        return left
class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        while left < right:
            capacity = (left + right) // 2

            days_needed = 1
            current_load = 0

            for weight in weights:
                if current_load + weight > capacity:
                    days_needed += 1
                    current_load = 0

                current_load += weight

            if days_needed <= days:
                right = capacity
            else:
                left = capacity + 1

        return left
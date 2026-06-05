class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(start, remaining, path):
            if remaining == 0:
                res.append(path[:])
                return

            for i in range(start, len(nums)):
                if nums[i] > remaining:
                    break

                path.append(nums[i])
                dfs(i, remaining - nums[i], path)  # reuse allowed
                path.pop()

        dfs(0, target, [])
        return res
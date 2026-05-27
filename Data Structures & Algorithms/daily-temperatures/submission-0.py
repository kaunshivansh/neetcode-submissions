class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                ans[idx] = i - idx

            stack.append(i)

        return ans
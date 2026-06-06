class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)

        if total % 4:
            return False

        target = total // 4

        matchsticks.sort(reverse=True)

        if matchsticks[0] > target:
            return False

        sides = [0] * 4

        def dfs(idx):
            if idx == len(matchsticks):
                return (
                    sides[0] == target and
                    sides[1] == target and
                    sides[2] == target and
                    sides[3] == target
                )

            stick = matchsticks[idx]

            for i in range(4):
                if sides[i] + stick > target:
                    continue

                sides[i] += stick

                if dfs(idx + 1):
                    return True

                sides[i] -= stick

                if sides[i] == 0:
                    break

            return False

        return dfs(0)
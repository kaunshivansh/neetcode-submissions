class Solution:
    def longestIncreasingPath(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            if dp[r][c]:
                return dp[r][c]

            max_len = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    max_len = max(max_len, 1 + dfs(nr, nc))

            dp[r][c] = max_len
            return max_len

        ans = 0
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, dfs(i, j))

        return ans
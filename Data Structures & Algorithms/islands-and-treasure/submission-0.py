from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    grid[nr][nc] == 2147483647
                ):
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
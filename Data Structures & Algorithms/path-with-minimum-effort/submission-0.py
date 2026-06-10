from heapq import heappush, heappop
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        effort = [[float('inf')] * cols for _ in range(rows)]
        effort[0][0] = 0

        heap = [(0, 0, 0)]  # (effort, row, col)

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while heap:
            curr_effort, r, c = heappop(heap)

            if r == rows - 1 and c == cols - 1:
                return curr_effort

            if curr_effort > effort[r][c]:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    edge = abs(heights[r][c] - heights[nr][nc])

                    new_effort = max(curr_effort, edge)

                    if new_effort < effort[nr][nc]:
                        effort[nr][nc] = new_effort
                        heappush(heap, (new_effort, nr, nc))

        return 0
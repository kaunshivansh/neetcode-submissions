from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        min_dist = [float('inf')] * n
        min_dist[0] = 0

        visited = [False] * n
        heap = [(0, 0)]  # (cost, node)

        total_cost = 0
        edges_used = 0

        while edges_used < n:
            cost, u = heapq.heappop(heap)

            if visited[u]:
                continue

            visited[u] = True
            total_cost += cost
            edges_used += 1

            x1, y1 = points[u]

            for v in range(n):
                if not visited[v]:
                    x2, y2 = points[v]

                    dist = abs(x1 - x2) + abs(y1 - y2)

                    if dist < min_dist[v]:
                        min_dist[v] = dist
                        heapq.heappush(heap, (dist, v))

        return total_cost
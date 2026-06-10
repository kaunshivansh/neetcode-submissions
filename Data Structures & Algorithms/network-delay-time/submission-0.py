from collections import defaultdict
from heapq import heappush, heappop
from typing import List

class Solution:
    def networkDelayTime(
        self,
        times: List[List[int]],
        n: int,
        k: int
    ) -> int:

        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        heap = [(0, k)]  # (time, node)

        while heap:
            curr_time, node = heappop(heap)

            if curr_time > dist[node]:
                continue

            for nei, weight in graph[node]:
                new_time = curr_time + weight

                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heappush(heap, (new_time, nei))

        max_time = max(dist[1:])

        return max_time if max_time != float('inf') else -1
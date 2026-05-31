import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = -heapq.heappop(heap)  # largest
            x = -heapq.heappop(heap)  # second largest

            if y != x:
                heapq.heappush(heap, -(y - x))

        return -heap[0] if heap else 0
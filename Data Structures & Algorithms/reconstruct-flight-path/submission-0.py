from collections import defaultdict
from heapq import heappush, heappop
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dst in tickets:
            heappush(graph[src], dst)

        itinerary = []

        def dfs(airport):
            while graph[airport]:
                nxt = heappop(graph[airport])
                dfs(nxt)

            itinerary.append(airport)

        dfs("JFK")

        return itinerary[::-1]
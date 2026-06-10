from collections import defaultdict, deque
from typing import List

class Solution:
    def buildMatrix(
        self,
        k: int,
        rowConditions: List[List[int]],
        colConditions: List[List[int]]
    ) -> List[List[int]]:

        def topo_sort(edges):
            graph = defaultdict(list)
            indegree = [0] * (k + 1)

            for u, v in edges:
                graph[u].append(v)
                indegree[v] += 1

            q = deque()

            for node in range(1, k + 1):
                if indegree[node] == 0:
                    q.append(node)

            order = []

            while q:
                node = q.popleft()
                order.append(node)

                for nei in graph[node]:
                    indegree[nei] -= 1

                    if indegree[nei] == 0:
                        q.append(nei)

            return order if len(order) == k else []

        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)

        if not row_order or not col_order:
            return []

        row_pos = {}
        col_pos = {}

        for i, num in enumerate(row_order):
            row_pos[num] = i

        for i, num in enumerate(col_order):
            col_pos[num] = i

        matrix = [[0] * k for _ in range(k)]

        for num in range(1, k + 1):
            matrix[row_pos[num]][col_pos[num]] = num

        return matrix